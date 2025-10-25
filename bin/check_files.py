#!/usr/bin/env python3

"""Tool to check that all files are being used

SPDX-License-Identifier: MIT
Copyright (C) 2025 Texas Instruments Incorporated - https://www.ti.com
"""

import argparse
import logging
import re
from pathlib import Path

logger = logging.getLogger(__name__)

SOURCE_PATH = Path("source/")
RST_SOURCE = sorted(SOURCE_PATH.glob("**/*.rst"))
IGNORED = re.compile(r"([^_].*\.rst)|(version\.txt)")


def get_paths(base):
    """Get a list of paths to check for, ignoring anything with a name that matches the IGNORED
    regex.

    :param base: Pathlib path to directory to search
    :return: List of pathlib paths
    """
    files_to_check = []
    for file in base.glob("**/*"):
        if file.is_dir():
            continue

        name = file.name
        if IGNORED.match(name):
            logger.debug("Ignored: %s", name)
            continue

        files_to_check.append(file)
    return files_to_check


def check_file(string, file):
    """Check to see if the given string appears in the file.

    :param string: String to look up
    :param file: Pathlib path to file
    :return: Boolean based on presence of string
    """
    pattern = re.compile(re.escape(string))
    text = file.read_text(encoding="utf-8")
    for _ in pattern.finditer(text):
        return True
    return False


def check_all(string):
    """Use an scan for any matches in RST_SOURCE files. Do not look for matches in the file itself.
    That last bit is particularly relevant for RST files that exist to be included in other files.

    :param string: String to look up
    :return: Boolean based on presence of string in any other files
    """
    for file in RST_SOURCE:
        if file == string:
            continue

        if check_file(string, file):
            return True
    return False


def get_unused_files(files):
    """Get a list of unused files from a subset of files given

    :param files: List of pathlib paths
    :return: List of unused pathlib paths
    """
    names_to_check = {x.name for x in files}
    unused_names = []
    for filename in names_to_check:
        if check_all(filename):
            continue

        logging.debug("Name not found: %s", filename)
        unused_names.append(filename)

    return [x for x in files if x.name in unused_names]


def main():
    """Main CLI entrypoint"""
    parser = argparse.ArgumentParser(
        prog="check_files.py",
        description="Tool to verify all files in the tree are in use",
    )

    parser.add_argument("-d", "--delete", action="store_true")
    parser.add_argument("-v", "--verbose", action="store_true")

    args = parser.parse_args()
    logging.basicConfig(level=logging.DEBUG if args.verbose else logging.INFO)

    files_to_check = get_paths(SOURCE_PATH)
    files_unused = get_unused_files(files_to_check)

    for path in files_unused:
        if args.delete:
            logging.info("Deleting: %s", path)
            path.unlink()
        else:
            logging.warning("File not used: %s", path)


if __name__ == "__main__":
    main()
