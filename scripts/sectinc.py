"""Scripts to prepare config values for Sphinx

SPDX-License-Identifier: MIT
Copyright (C) 2025 Texas Instruments Incorporated - https://www.ti.com
"""

import re
from pathlib import Path


def generate_include_patterns(family_configlist):
    """Read the toc.txt file and generate an include_patterns list for Sphinx

    :param family_configlist: List of String paths to the toc.txt files
    """
    comment = re.compile(r"#.*")
    include_files = []
    for config in family_configlist:
        config_path = Path("configs").joinpath(config)
        with config_path.open("r", encoding="utf-8") as config_file:
            for line in config_file:
                clean_line = comment.sub("", line).strip()
                if clean_line:
                    include_files.append(clean_line + ".rst")
    return include_files
