#!/usr/bin/python
# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Google's Python Class
# http://code.google.com/edu/languages/google-python-class/

import sys
import re
import os
import shutil
import subprocess

"""Copy Special exercise
"""

# +++your code here+++
# Write functions and modify main() to call them


def get_special_paths(dir):
    paths = []
    pattern = "\w+__\w+__.\w{3}"
    for root, dirs, files in os.walk(dir):
        for file in files:
            match = re.search(pattern, file)
            if match:
                paths.append(os.path.abspath(root + r'\\' + file))

    return paths


def copy_to(paths, dir):
    for file in paths:
        destFile = os.path.join(dir, os.path.basename(file))
        print('Copying %s to %s...' % (file, destFile))
        shutil.copy(file, destFile)

    return


def zip_to(paths, zippath):
    for file in paths:
        print('Adding %s to archive: %s' % (file, zippath))

    return


def main():
    # This basic command line argument parsing code is provided.
    # Add code to call your functions below.

    # Make a list of command line arguments, omitting the [0] element
    # which is the script itself.
    args = sys.argv[1:]
    if not args:
        print("usage: [--todir dir][--tozip zipfile] dir [dir ...]")
        sys.exit(1)

    # todir and tozip are either set from command line
    # or left as the empty string.
    # The args array is left just containing the dirs.
    todir = ''
    if args[0] == '--todir':
        todir = args[1]
        del args[0:2]

    tozip = ''
    if args[0] == '--tozip':
        tozip = args[1]
        del args[0:2]

    if len(args) == 0:
        print("error: must specify one or more dirs")
        sys.exit(1)

    # +++your code here+++
    # Call your functions
    special_paths = get_special_paths(args[0])

    if len(todir) > 0:
        copy_to(special_paths, todir)

    if len(tozip) > 0:
        zip_to(special_paths, tozip)


if __name__ == "__main__":
    main()
