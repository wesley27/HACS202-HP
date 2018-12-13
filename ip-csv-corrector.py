#!/usr/bin/python
import sys
import re

"""
When designing the ip-information extraction script the
idea of including the count of IP addresses within the
same CSV file as the rest of the IP data was somehow 
missed, and it was decided that the IP frequencies would
be logged to another file.

This was silly.

It was later (as of now) deemed that in the interest of well-
managed time it would be faster to simply write a script to
combine the frequency information into the CSV file, rather 
than to redesign the extraction script to combine these files.

This script is the result.

Usage: ./ip-csv-converter.py
Run this script from the same directory as ipdata.csv and
frequencies.txt.
"""

CSV_NAME = 'ipdata.csv'
FRQ_NAME = 'frequencies.txt'

def correct_csv():
    ipcounts = {}

    fr = open(FRQ_NAME)
    for line in fr:
        ipc = re.match('^IP: (?P<IP_Address>[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3})\s+Count: (?P<Count>[0-9]+)\n', line)
        if ipc != None:
            ipcounts[ipc.groupdict()['IP_Address']] = ipc.groupdict()['Count']
    fr.close()

    csvlines = []
    cs = open(CSV_NAME)
    for line in cs:
        csvlines.append(line)
    cs.close()
    
    cs = open(CSV_NAME, 'w')
    for line in csvlines:
        if 'IP_address,city' in line:
            newline = 'count,' + line
            cs.write(newline)
        else:
            ip = line.split(',')[0]
            newline = ipcounts[ip] + ',' + line
            cs.write(newline)
    cs.close()

if __name__ == '__main__':
    if len(sys.argv) != 1:
        print('Incorrect usage. Try ./ip-csv-converter.py')
    else:
        correct_csv()
