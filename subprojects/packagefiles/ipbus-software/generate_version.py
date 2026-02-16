#!/usr/bin/env python3

import argparse
import getpass
import platform
import time

parser = argparse.ArgumentParser()
parser.add_argument("input")
parser.add_argument("output")
parser.add_argument("version")
args = parser.parse_args()

major, minor, patch = args.version.split('.')

with open(args.input, "rt") as input_file:
    lines = input_file.read()

    lines = lines.replace("__PROJECT_VERSION_MAJOR__", major)
    lines = lines.replace("__PROJECT_VERSION_MINOR__", minor)
    lines = lines.replace("__PROJECT_VERSION_PATCH__", patch)
    lines = lines.replace("__LOCAL_BUILD_HOSTNAME__", platform.node())
    lines = lines.replace("__LOCAL_BUILD_USERNAME__", getpass.getuser())
    lines = lines.replace("__BUILDTIME_SECONDS_SINCE_EPOCH__", str(int(time.time())))

    with open(args.output, "wt") as output_file:
        output_file.write(lines)
