#!/usr/bin/python
import csv
import os
import sys
import re

"""
This file extracts data from the session files in ./attacker_sessions
and formats it into a clean, usable CSV file.

Usage: ./dextract-sessioninfo.py
"""

CSV_NAME = 'session_data.csv'

def extract_session_data():
    csv = open(CSV_NAME, 'wb+')
    filewrite = csv.write(csv, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL)
    filewriter.writerow([]) # column headers

    session_pattern = re.compile('^[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}')

    for filename in os.listdir(os.getcwd()):
        if not session_pattern.match(filename):
            continue

        session_file = open(filename)
        for line in session_file:
            #process file line by line

        session_file.close()

    csv.close()

if __name__ == '__main__':
    if len(sys.argv) > 1:
        print('Invalid arguments. Proper usage is ./dextract-sessioninfo.py')
    else:
        extract_session_data()
