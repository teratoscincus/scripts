#!/usr/bin/env zsh

# Change directory and activate Pipenv venv if a Pipfile is present.

PIPFILE='Pipfile'

cd "$1" || exit

# Check for Pipenv venv
if [[ -f "$PIPFILE" ]]; then
	pipenv shell
fi
