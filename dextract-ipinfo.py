#!/usr/bin/env python
import subprocess
import sys

"""
This script handles the processing of attacker session files to obtain
IP address information and statistics. It outputs this data to CSV.

Proper usage:
./dextract-ipinfo.py
"""

def extract_ip_data():
    print('extract here')

if __name__ == '__main__':
    if len(sys.argv) > 1:
        print('Invalid arguments. Proper usage is ./dextract-ipinfo.py')
    else:
        extract_ip_data()
