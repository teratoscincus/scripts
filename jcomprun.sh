#!/usr/bin/env bash

# Run java snippets
# The script takes the name of a .java file (including the file extension) as a first
# possitonal argument:
#     jcomprun.sh Sandbox.java

javac "$1" && java "${1::-5}" "${@:2}"
