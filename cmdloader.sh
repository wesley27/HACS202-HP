#!/bin/bash
#
# This script loads necessary commands into the user
# script directory for programmatic usage as system commands.

# Enabling scripts to be called as system commands eliminates
# the need for loading them as imports.
cp mitm-ssr /usr/local/bin/
cp honeypot.py /usr/local/bin/
