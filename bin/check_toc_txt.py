#!/usr/bin/env python3

"""Tool to verify all files in the given toc are valid

SPDX-License-Identifier: MIT
Copyright (C) 2025 Texas Instruments Incorporated - https://www.ti.com
"""

import argparse
import re
from pathlib import Path
import logging

CONFIG_PATH = Path("configs/")
SOURCE_PATH = Path("source/")
COMMENT_REGEX = re.compile(r"#.*")

logger = logging.getLogger(__name__)


def get_slug_path(slug):
    """Convert the given slug to a pathlib path. Assumes extension will be rst.

    :param slug: String path slug
    """
    path = SOURCE_PATH.joinpath(slug + ".rst")
    logging.debug("Expanded slug: %s", path)
    return path


def process_toc_txt(path):
    """Process a single toc.txt file

    :param path: Pathlib path to toc.txt
    :return: Set of valid paths
    """
    valid_paths = set()
    with path.open("r", encoding="utf-8") as file:
        logging.debug("Processing %s", path)
        for line_number, line in enumerate(file):
            clean_line = COMMENT_REGEX.sub("", line).strip()
            if clean_line:
                slug_path = get_slug_path(clean_line)
                if slug_path.is_file():
                    valid_paths.add(slug_path)
                else:
                    logging.warning(
                        "Invalid slug: %s:%i %s", path, line_number + 1, clean_line
                    )
    return valid_paths


def process_src_tree(toc_paths):
    """Ensure all RST files in the src tree are listed in the given set"""
    src_paths = set()
    for path in SOURCE_PATH.glob("**/*.rst"):
        # files that begin with an underscore are included by other rst files
        # they should not be listed in the toc
        if path.stem[0] != "_":
            src_paths.add(path)
    for path in src_paths - toc_paths:
        logging.warning("File not in any toc: %s", path)


def process_all():
    """Process all toc.txt files in the config directory"""
    toc_paths = set()
    for path in CONFIG_PATH.glob("**/*toc.txt"):
        if path.is_file():
            toc_paths |= process_toc_txt(path)
    process_src_tree(toc_paths)


def main():
    """Main CLI entrypoint"""
    parser = argparse.ArgumentParser(
        prog="check_toc_txt.py",
        description="Tool to verify all files in the given toc are valid",
    )

    parser.add_argument("-t", "--toc", type=Path)
    parser.add_argument("-v", "--verbose", action="store_true")

    args = parser.parse_args()
    log_level = logging.DEBUG if args.verbose else logging.INFO
    logging.basicConfig(level=log_level)

    if args.toc:
        if not args.toc.is_file():
            logging.critical("Invalid toc.txt file specified")
        process_toc_txt(args.toc)
    else:
        process_all()


if __name__ == "__main__":
    main()
