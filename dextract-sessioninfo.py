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
    csvout = open(CSV_NAME, 'ab+')
    filewriter = csv.writer(csvout, delimiter='%', quotechar='|', quoting=csv.QUOTE_MINIMAL)
    if not os.path.isfile(CSV_NAME) or os.path.getsize(CSV_NAME) <= 0:
        filewriter.writerow(['timestamp', 's_id', 'c_id', 'atk_ip', 'atk_cmd', 'atk_output']) # column headers

    session_pattern = re.compile('^[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}')

    for filename in os.listdir(os.getcwd()):
        if not session_pattern.match(filename):
            continue

        print('Now processing: %s' % (filename))
        session_file = open(filename)
        timestamp = ''
        s_id = filename
        c_id = ''
        atk_ip = ''
        atk_cmd = []
        atk_output = []
        at_output = False
        for line in session_file:
            #process file line by line
            if filename in line:
                at_output = False
            elif 'Date: 2018' in line:
                dat = line.split(': ')
                timestamp = dat[1][:-1]
            elif 'Container ID:' in line:
                dat = line.split(': ')
                c_id = dat[1][:-1]
            elif 'Attacker IP' in line:
                dat = line.split(': ')
                atk_ip = dat[1][:-1]
            elif 'command' in line:
                dat = line.split(': ')
                if len(dat) > 1:
                    atk_cmd.append(dat[1][:-1])
            elif 'root@CT10' in line:
                dat = line.split(':~# ')
                atk_cmd.append(dat[1][:-1])
            elif 'Output Below' in line:
                at_output = True
                continue
            elif at_output:
                atk_output.append(line[:-2])
        
        filewriter.writerow([timestamp, s_id, c_id, atk_ip, str(atk_cmd), str(atk_output)])
        session_file.close()

    csvout.close()

if __name__ == '__main__':
    if len(sys.argv) > 1:
        print('Invalid arguments. Proper usage is ./dextract-sessioninfo.py')
    else:
        extract_session_data()
