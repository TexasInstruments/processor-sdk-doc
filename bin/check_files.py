#!/usr/bin/env python3

"""Tool to check that all files are being used

SPDX-License-Identifier: MIT
Copyright (C) 2025 Texas Instruments Incorporated - https://www.ti.com
"""

import logging
import re
from pathlib import Path

logger = logging.getLogger(__name__)

SOURCE_PATH = Path("source/")
RST_SOURCE = sorted(SOURCE_PATH.glob("**/*.rst"))
IGNORED = re.compile(r"([^_].*\.rst)|(version\.txt)")


def get_names(base):
    """Get a set of file names to check for, ignoring anything in that matches the IGNORED regex.

    :param base: Pathlib path to directory to search
    :return: Set of string path names
    """
    files_to_check = set()
    for file in base.glob("**/*"):
        if file.is_dir():
            continue

        name = file.name
        if IGNORED.match(name):
            logger.debug("Ignored: %s", name)
            continue

        files_to_check.add(name)
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


def main():
    """Main CLI entrypoint"""
    logging.basicConfig(level=logging.INFO)

    files_to_check = get_names(SOURCE_PATH)
    for filename in files_to_check:
        if check_all(filename):
            continue
        logging.info("File not used: %s", filename)


if __name__ == "__main__":
    main()
