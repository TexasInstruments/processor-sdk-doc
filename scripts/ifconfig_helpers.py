"""Helper functions to guard against incorrect ifconfig usage

SPDX-License-Identifier: MIT
Copyright (C) 2025 Texas Instruments Incorporated - https://www.ti.com
"""

import re
import sys
from pathlib import Path

# This is not a full regular expression for config values, as '\' is valid, but it's good enough for
# the processing below
_CONFIG_REGEX = re.compile(r"'(CONFIG_.*)'\s*:\s*'(.*)'")


def _load_internal_set(path):
    """Populate the internal set we use to check that the expected values are sane

    :param path: Pathlib path to config directory
    """
    internal_set_dict = {}
    if not path.is_dir():
        return internal_set_dict

    for config_path in path.glob("**/*_config.txt"):
        with config_path.open("r", encoding="utf-8") as file:
            for line in file:
                match = _CONFIG_REGEX.match(line)
                if match:
                    key = match.group(1)
                    key_set = internal_set_dict.get(key, set())
                    key_set.add(match.group(2))
                    internal_set_dict[key] = key_set

    return internal_set_dict


_INTERNAL_SET_DICT = _load_internal_set(
    Path(__file__).parent.parent.joinpath("configs/")
)


def key_within(config, expected):
    """Check if the values specified are all valid and return if the value of the config option is
    in that set

    :param config: Config value in current scope
    :param expected: Any iterable set of values expected to be in the key
    """
    real_set = set(expected)
    if not real_set.issubset(_INTERNAL_SET_DICT[config]):
        raise ValueError(f"Given expectations are unreasonable for '{config}'")

    return locals()[config] in expected


class CollisionException(Exception):
    """Exception class to indicate when a function definition collision occurs"""


if __builtins__.get("key_within") is not None:
    raise CollisionException("Function collides with an existing definition")

__builtins__["key_within"] = key_within
