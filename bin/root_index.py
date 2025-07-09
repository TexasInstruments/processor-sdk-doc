#!/usr/bin/env python3

"""Tool to find and make a index of doc root index files

SPDX-License-Identifier: MIT
Copyright (C) 2025 Texas Instruments Incorporated - https://www.ti.com
"""

from pathlib import Path
import logging
from jinja2 import Environment, FileSystemLoader

BUILD_PATH = Path("build/")
TEMPLATE_PATH = Path(__file__).parent

logger = logging.getLogger(__name__)


def get_root_index(path):
    """Get the root index from a list of candidates

    :param path: Pathlib path to search in
    """
    candidates = [x for x in path.glob("**/index.html") if x.is_file()]
    if not candidates:
        return None

    sorted_paths = sorted(candidates, key=lambda x: len(x.parts))
    return sorted_paths[0]


def get_index_list():
    """Get the list of index files to use from the build directory"""
    index_list = []
    for path in BUILD_PATH.glob("*/"):
        root = get_root_index(path)
        if root:
            logging.info("Found index: %s", root)
            root = root.relative_to(BUILD_PATH)
            logging.info("Updating path to: %s", root)
            index_list.append(root)
    return sorted(index_list)


def generate_root_index(index_list):
    """Make the root index file

    :param index_list: List of pathlib paths to indexes
    """
    root_index_path = BUILD_PATH.joinpath("index.html")
    logging.info("Loading jinja env")
    env = Environment(loader=FileSystemLoader(TEMPLATE_PATH))
    template = env.get_template("root_index.html")
    logging.info("Using template: %s", template.name)
    output = template.render(path_list=index_list)
    logging.info("Writing output to: %s", root_index_path)
    with root_index_path.open("w", encoding="utf-8") as f:
        f.write(output)


def main():
    """Main processing loop"""
    logging.basicConfig(level=logging.INFO)
    index_list = get_index_list()
    generate_root_index(index_list)


if __name__ == "__main__":
    main()
