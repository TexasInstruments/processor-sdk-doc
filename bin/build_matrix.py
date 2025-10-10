#!/usr/bin/env python3

"""Tool to create a build matrix for the current tree

SPDX-License-Identifier: MIT
Copyright (C) 2025 Texas Instruments Incorporated - https://www.ti.com
"""

import json
import logging
import os
from pathlib import Path

CONFIG_PATH = Path("configs/")
GITHUB_PATH = Path(os.environ.get("GITHUB_OUTPUT", "test_output.txt"))
REQUIRED_CONFIG_FRAGMENTS = {"config.txt", "tags.py", "toc.txt"}
logger = logging.getLogger(__name__)


def output_matrix(matrix):
    """Write the output of the matrix to the GitHub CI managed file

    :param matrix: List of dictionaries of valid os and platform combinations
    """
    matrix_string = json.dumps(matrix)
    logging.info("Writing matrix data to: %s", GITHUB_PATH)
    with GITHUB_PATH.open("a", encoding="utf-8") as file:
        file.write(f"matrix={matrix_string}\n")


def unpack_os_set(platform, os_set):
    """Produce a list of dictionaries of valid platform to os mappings.

    :param platform: String name of platform to use
    :param os_set: Set of string os names supported
    :return: List of dictionaries with os and platform mappings
    """
    platform_matrix = []
    for name in os_set:
        platform_matrix.append({"device": platform, "os": name})
    return platform_matrix


def valid_os_set(platform):
    """Get a set of valid OS options for a give platform path. This is a little more complex than it
    needs to be so that we can produce some more verbose warnings.

    :param platform: Pathlib path to platform config directory
    :return: Set of valid OS options
    """
    config_fragments = set()
    for fragment in REQUIRED_CONFIG_FRAGMENTS:
        config_fragments |= {
            x.name for x in platform.glob(f"{platform.stem}_*_{fragment}")
        }

    os_names = set()
    for name in config_fragments:
        os_names.add(name.split("_")[1])

    valid_os = set()
    for name in os_names:
        invalid = False
        for fragment in REQUIRED_CONFIG_FRAGMENTS:
            required_file = f"{platform.stem}_{name}_{fragment}"
            if required_file not in config_fragments:
                invalid = True
                logging.warning("Missing the required file: %s", required_file)

        if invalid:
            logging.warning("Skipping the invalid OS: %s", name)
        else:
            valid_os.add(name)

    return valid_os


def main():
    """Main processing loop"""
    logging.basicConfig(level=logging.INFO)

    matrix_list = []
    for platform in CONFIG_PATH.glob("*/"):
        if not platform.is_dir():
            continue
        logging.info("Parsing platform at: %s", platform)
        os_set = valid_os_set(platform)
        matrix_list.extend(unpack_os_set(platform.stem, os_set))

    output_matrix(matrix_list)


if __name__ == "__main__":
    main()
