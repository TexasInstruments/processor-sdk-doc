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


def is_slug(slug):
    """Check to see if the given slug is valid. Assumes extension will be rst.

    :param slug: String path slug
    """
    path = SOURCE_PATH.joinpath(slug + ".rst")
    logging.debug("Expanded slug: %s", path)
    return path.is_file()


def process_toc_txt(path):
    """Process a single toc.txt file

    :param path: Pathlib path to toc.txt
    """
    with path.open("r", encoding="utf-8") as file:
        logging.debug("Processing %s", path)
        for line_number, line in enumerate(file):
            clean_line = COMMENT_REGEX.sub("", line).strip()
            if clean_line and not is_slug(clean_line):
                logging.warning("Invalid slug: %s:%i %s", path, line_number + 1, clean_line)


def process_all():
    """Process all toc.txt files in the config directory"""
    for path in CONFIG_PATH.glob("**/*toc.txt"):
        if path.is_file():
            process_toc_txt(path)


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
