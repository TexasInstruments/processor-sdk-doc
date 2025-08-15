#!/usr/bin/env python3

"""Tool to deduplicate HTML assets for GitHub pages deployments

SPDX-License-Identifier: MIT
Copyright (C) 2025 Texas Instruments Incorporated - https://www.ti.com
"""

import argparse
import logging
from multiprocessing import Pool

from lxml import html
from root_index import get_root_index, BUILD_PATH

COMMON_PATHS = {"_images", "_downloads", "_static"}


def _rewrite_path(html_path, common_dir, check_list):
    """Wrapper to replace links using lxml rewrite_links. Defines a throwaway function to make
    things faster.

    :param html_path: Pathlib path to file to HTML file
    :param common_dir: Pathlib path to the document root directory
    :param check_list: Iterable of pathlib paths to check
    """
    with html_path.open("r", encoding="utf-8") as file:
        document = html.fromstring(file.read())

    old_rel_path = html_path.parent.resolve()
    new_rel_path = common_dir.resolve()

    def _update_link(link):
        """Function to interact with lxml's rewrite_links

        :param link: String link to rewrite
        """
        clean_link = link.strip()
        if clean_link[:4] == "http":
            return link

        link_path = old_rel_path.joinpath(clean_link).resolve()
        for check_path in check_list:
            if link_path.is_relative_to(check_path):
                logging.info("rewriting link in: %s", html_path)
                logging.debug("old link path: %s", link_path)
                new_path = new_rel_path.joinpath(
                    link_path.relative_to(check_path.parent)
                )
                logging.debug("new link path: %s", new_path)
                rel_path = new_path.relative_to(old_rel_path, walk_up=True)
                logging.debug("new rel path: %s", rel_path)
                logging.debug("---")
                return rel_path.as_posix()

        return link

    document.rewrite_links(_update_link, resolve_base_href=False)

    with html_path.open("wb") as file:
        file.write(
            html.tostring(
                document,
                encoding="utf-8",
                include_meta_content_type=True,
                doctype="<!DOCTYPE html>",
            )
        )


def _move_files(old_rel_path, new_rel_path, check_list):
    """Move the files that match the check_list from the old_rel_path root into new_rel_path.

    :param old_rel_path: Pathlib path to the document root directory
    :param new_rel_path: Pathlib path to the new common directory
    :param check_list: Iterable of pathlib paths to check
    """
    for check_path in check_list:
        operating_dir = old_rel_path.joinpath(check_path)
        for path in operating_dir.glob("**/*"):
            if not path.is_file():
                continue
            rel = path.relative_to(old_rel_path)
            logging.info("moving file: %s", rel)
            new = new_rel_path.joinpath(rel)
            logging.debug("destination: %s", new)
            new.parent.mkdir(mode=0o755, parents=True, exist_ok=True)
            path.replace(new)

        for empty_dir in sorted(operating_dir.glob("**/*"), reverse=True):
            empty_dir.rmdir()


def rewrite_paths(root_dir, common_dir, jobs):
    """Rewrite the paths to move assets into a common_dir directory. This assumes:

    1. Paths are already relative to the given root_dir
    2. The root_dir resides under the common_dir

    :param root_dir: Pathlib path to document root directory
    :param common_dir: Pathlib path to new common_dir directory
    """
    check_list = {root_dir.joinpath(x).resolve() for x in COMMON_PATHS}
    logging.info("rewriting paths")
    starmap_iterable = [
        (path, common_dir, check_list) for path in root_dir.glob("**/*.html")
    ]
    with Pool(jobs) as pool:
        pool.starmap(_rewrite_path, starmap_iterable)
    logging.info("moving the files")
    _move_files(root_dir.resolve(), common_dir.resolve(), check_list)


def main():
    """Main processing loop"""
    parser = argparse.ArgumentParser(
        prog="dedupe.py",
        description="Tool to deduplicate HTML assets for GitHub pages deployments",
    )

    parser.add_argument("-v", "--verbose", action="store_true")
    parser.add_argument("-j", "--jobs", type=int, default=8)

    args = parser.parse_args()

    logging.basicConfig(level=logging.DEBUG if args.verbose else logging.INFO)

    root_list = []
    for path in BUILD_PATH.glob("*/"):
        index_path = get_root_index(path)
        if index_path:
            root_list.append(index_path.parent)
            logging.info("found the following index: %s", index_path)

    for path in root_list:
        logging.info("working on the following document dir: %s", path)
        rewrite_paths(path, BUILD_PATH, args.jobs)


if __name__ == "__main__":
    main()
