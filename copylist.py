#!/usr/bin/env python3

"""
A script to copy files and directories from users home directory to the CWD from which
the script is called.

Usage:
    Reads in file and directory names to be copied from `COPYLIST_FILE` in current
    working directory from where this script is called.
    File and directories listed in `COPYLIST_FILE` are expected to be paths relative to
    the users home directory.

    Ensure the directory containing this script is in PATH, for ease of use.

Comment out lines in list:
    Files and directories can be commented out using "#" in `COPYLIST_FILE`.
"""

import os
import subprocess
from pathlib import Path

COPYLIST_FILE = ".copylist.txt"

CWD = Path(os.getcwd())
HOME = Path(os.path.expanduser("~"))

# Output color formatting.
B_RED = "\033[1;31m"
B_GREEN = "\033[1;32m"
B_BLUE = "\033[1;34m"
COLOR_OFF = "\033[0m"


def copy_dirs(copy_list: list):
    for content in copy_list:
        content = content.rstrip("\n")
        if content.startswith("#") or content == "":
            continue
        if not os.path.exists(HOME / content):
            continue
        # Copy recursively to CWD.
        print(f"Copying {content}")
        subprocess.run(["cp", "-rt", CWD, HOME / content])
        print(f"{B_GREEN}Copied{COLOR_OFF} {content}")
    print(f"\n{B_GREEN}Done copying!{COLOR_OFF}")


if __name__ == "__main__":
    with open(CWD / COPYLIST_FILE, "r") as f:
        copy_list = f.readlines()

    print(f"Destination: {B_BLUE}{CWD}{COLOR_OFF}")
    print("Files and directories to be copied:")
    for content in copy_list:
        content = content.rstrip("\n")
        if content.startswith("#") or content == "":
            continue
        if not os.path.exists(HOME / content):
            print(f"{B_RED}Not found: ~/{content}")
        print(f"~/{content}")
    confirmation = input("\nProceed? (y/n) ").strip().lower()

    if confirmation == "y":
        copy_dirs(copy_list)
