"""Scripts to prepare config values for Sphinx

SPDX-License-Identifier: MIT
Copyright (C) 2025 Texas Instruments Incorporated - https://www.ti.com
"""

import re
from pathlib import Path


def generate_exclude_patterns(family_configlist):
    """Read the toc.txt file and generate an exclude_patterns list for Sphinx. We use
    exclude_patterns instead of include_patterns so toc.not_readable errors are specifically about
    paths used with the RST toctree directive in the source directory.

    :param family_configlist: List of String paths to the toc.txt files
    """
    comment = re.compile(r"#.*")
    include_files = set()
    for config in family_configlist:
        config_path = Path("configs").joinpath(config)
        with config_path.open("r", encoding="utf-8") as config_file:
            for line in config_file:
                clean_line = comment.sub("", line).strip()
                if clean_line:
                    clean_line = clean_line + ".rst"
                    include_files.add(clean_line)
    if not include_files:
        raise ValueError("Expected at least one entry in the toc.txt file")
    all_rst_files = set(
        x.relative_to("source/").as_posix() for x in Path("source/").glob("**/*.rst")
    )
    exclude_files = all_rst_files.difference(include_files)
    return list(exclude_files)
