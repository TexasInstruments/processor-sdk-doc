#!/usr/bin/env python3

"""Simple helper for renaming files and fixing up refs

SPDX-License-Identifier: MIT
Copyright (C) 2025 Texas Instruments Incorporated - https://www.ti.com

This enforces relative pathing, which is not only preferred by RST but it plays better with
rstcheck.
"""

import argparse
import logging
import re
import subprocess
from multiprocessing import Pool
from pathlib import Path

CONFIG_PATH = Path("configs/")
SOURCE_PATH = Path("source/")
logger = logging.getLogger(__name__)


class LineFilter:
    """Wrapper class for registering and utilizing multiple string filters on a file"""

    filter_list = []
    dryrun = True

    def __init__(self):
        return

    def register(self, function):
        """Register the given filter function. This function will be passed a series of named
        arguments corresponding to the file and line being parsed. It must at least process handle
        the line argument and return an unmodified or modified line.

        :param function: A function that at least takes a line named argument and returns a line
        """
        function(line="A", file=Path("."))
        self.filter_list.append(function)

    def set_dryrun(self, dryrun):
        """Update the internal dryrun variable

        :param dryrun:
        """
        self.dryrun = dryrun

    def filter(self, file):
        """Parse the given file with all registered filters

        :param file: Pathlib Path to file
        """
        text = file.read_text()
        result = []
        modified = False
        for line in text.splitlines(True):
            result_line = line
            for filter_function in self.filter_list:
                result_line = filter_function(line=result_line, file=file)
            if line != result_line:
                if self.dryrun:
                    logger.info(
                        "Would modify:%s:%s:%s", file, line.strip(), result_line.strip()
                    )
                else:
                    logger.info(
                        "Modifying:%s:%s:%s", file, line.strip(), result_line.strip()
                    )
                modified = True
            if not self.dryrun:
                result.append(result_line)
        if modified and not self.dryrun:
            file.write_text("".join(result))


def git_rename(source, destination, dryrun):
    """Wrapper and logger for git rename

    :param source: Pathlib path to source file
    :param destination: Pathlib path to destination file
    :param dryrun: Bool to toggle writing files
    """
    command = ["git", "mv"]
    if dryrun:
        command.append("--dry-run")
    command.extend([source, destination])
    result = subprocess.run(command, capture_output=True, check=True, text=True)
    for line in result.stdout.splitlines():
        logging.info("git:%s", line)


def update_file_contents(file, pattern, new, dryrun):
    """Update given file changing all instances of pattern to new string

    :param file: Pathlib path to source file
    :param pattern: Regex pattern to match against
    :param new: String to replace the regex expression with
    :param dryrun: Bool to toggle writing files
    """
    logging.debug("Reading:%s", file)
    text = file.read_text()
    log_str = "Would modify" if dryrun else "Modifying"
    for match in pattern.finditer(text):
        logging.info("%s:%s:%s:%s", log_str, file, match.group(0).strip(), new.strip())
    if dryrun:
        return
    result = []
    for line in text.splitlines(True):
        result.append(pattern.sub(new, line))
    file.write_text("".join(result))


def multiprocessing_handler(command, command_args, jobs):
    """Simple wrapper to handle job parallelization

    :param command: Function to execute in the pool
    :param command_args: Map of arguments for each execution
    :param jobs: Integer count of threads to use
    """
    with Pool(jobs) as pool:
        pool.starmap(command, command_args)


def update_configs(source, destination, dryrun, jobs):
    """Check all files for any old refs

    :param source: Pathlib path to source file
    :param destination: Pathlib path to destination file
    :param dryrun: Bool to toggle writing files
    :param jobs: Integer count of threads to use
    """
    file_list = [path for path in CONFIG_PATH.glob("**/*.txt") if path.is_file()]
    file_list.extend([path for path in CONFIG_PATH.glob("**/*.py") if path.is_file()])
    config_source = source.parent.relative_to(SOURCE_PATH).joinpath(source.stem)
    config_destination = (
        destination.parent.relative_to(SOURCE_PATH)
        .joinpath(destination.stem)
        .as_posix()
        + "\n"
    )
    pattern = re.compile(r"(" + re.escape(config_source.as_posix()) + r"){1}(\s+|$)")
    logging.debug("config_pattern:%s", pattern)
    mapping = [(file, pattern, config_destination, dryrun) for file in file_list]
    multiprocessing_handler(update_file_contents, mapping, jobs)


def register_rst_filters(source, destination):
    """Register all rst related filters and bake any known constants

    :param source: Pathlib path to source file
    :param destination: Pathlib path to destination file
    """
    filter_handler = LineFilter()

    inc_pattern = re.compile(
        r"(\s*\.\. [^:]*::)(.*)(" + re.escape(source.name) + r")(\s|$)"
    )

    def update_directives(**kwargs):
        """Replace old include and image/figure statements"""
        ref_destination = (
            ' '
            + destination.relative_to(kwargs["file"], walk_up=True).as_posix()
            + "\n"
        )

        line = kwargs["line"]
        regex_match = inc_pattern.match(line)
        if regex_match:
            line = regex_match.group(1) + ref_destination

        return line

    filter_handler.register(update_directives)

    inl_pattern = re.compile(r"(`[^`]*)(" + re.escape(source.stem) + r")([^`]*`)")

    def update_inlines(**kwargs):
        """Replace inline refrences"""
        ref_destination = (
            "`"
            + destination.with_suffix("")
            .relative_to(kwargs["file"], walk_up=True)
            .as_posix()
            + "`"
        )
        return inl_pattern.sub(ref_destination, kwargs["line"])

    filter_handler.register(update_inlines)

    toc_pattern = re.compile(
        r"(\s+)(\S*)(" + re.escape(source.stem) + r")(.rst)?(\s+|$)"
    )

    def update_toctree(**kwargs):
        """Replace toctree entries"""
        ref_destination = (
            destination.with_suffix("")
            .relative_to(kwargs["file"].parent, walk_up=True)
            .as_posix()
            + "\n"
        )

        line = kwargs["line"]
        regex_match = toc_pattern.match(line)
        if regex_match:
            line = regex_match.group(1) + ref_destination

        return line

    filter_handler.register(update_toctree)
    return filter_handler


def unique_tail(file):
    """Return if the file has a unique name and extension

    :param file: Pathlib path to file
    """
    path_names = [
        path.name for path in SOURCE_PATH.glob(f"**/{file.name}") if path.is_file()
    ]
    return path_names.count(file.name) <= 1


def warn_unique_tail(file):
    """Warn the user if a given tail is not unique

    :param file: Pathlib path to file
    """
    if not unique_tail(file):
        logger.warning("File tail is not unique, check diff carefully:%s", file)


def rename(source, destination, dryrun, jobs):
    """Main processing context

    :param source: Pathlib path to source file
    :param destination: Pathlib path to destination file
    :param dryrun: Bool to toggle writing files
    :param jobs: Integer count of threads to use
    """
    if source.exists():
        warn_unique_tail(source)
        warn_unique_tail(destination)
        git_rename(source, destination, dryrun)
        filter_handler = register_rst_filters(source, destination)
        filter_handler.set_dryrun(dryrun)
        file_list = [[path] for path in SOURCE_PATH.glob("**/*.rst") if path.is_file()]
        multiprocessing_handler(filter_handler.filter, file_list, jobs)

        update_configs(source, destination, dryrun, jobs)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        prog="rename.py", description="File rename helper for processor-sdk-doc"
    )

    parser.add_argument("source", type=Path)
    parser.add_argument("destination", type=Path)
    parser.add_argument("-n", "--no-dry-run", action="store_false")
    parser.add_argument("-v", "--verbose", action="store_true")
    parser.add_argument("-j", "--jobs", type=int, default=8)

    args = parser.parse_args()

    LOG_LEVEL = logging.DEBUG if args.verbose else logging.INFO
    logging.basicConfig(level=LOG_LEVEL)
    rename(args.source, args.destination, args.no_dry_run, args.jobs)
