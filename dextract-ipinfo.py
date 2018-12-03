#!/usr/bin/env python
import subprocess
import sys
import os
import re
from urllib2 import urlopen
import json
import csv


"""
This script handles the processing of attacker session files to obtain
IP address information and statistics. It outputs this data to a csv
file that can be found at ./ipdata.csv. It also outputs a frequency
chart for all IPs found.

Proper usage:
./dextract-ipinfo.py
"""

STR_ATK_IP = 'Attacker IP Address:'

def extract_ip_data():
    session_pattern = re.compile('^[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}')
    csvout = open('ipdata.csv', 'wb')
    filewriter = csv.writer(csvout, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL)
    filewriter.writerow(['IP_address', 'city', 'country', 'IP_org'])
    ip_counts = []
    count = 0
    for filename in os.listdir(os.getcwd()):
        if session_pattern.match(filename):
            with open(filename) as f:
                for line in f.readlines():
                    if STR_ATK_IP in line:
                        ip = line.split(': ')[1][:-1]
                        found = 0
                        for (num, ipv) in ip_counts:
                            if ipv == ip:
                                ip_counts[ip_counts.index((num, ipv))] = (num + 1, ipv)
                                found = 1
                                break
                        if found == 0:
                            ip_counts.append((1, ip))

                        STR_IP_LKUP = 'http://ipinfo.io/%s' % (ip)
                        response = urlopen(STR_IP_LKUP)
                        ipdata = json.load(response)
                        city = ipdata['city']
                        country = ipdata['country']
                        org = ipdata['org']
                        filewriter.writerow([ip, city, country, org])
                        count += 1
                f.close()
    csvout.close()
    print('Processed %d IP addresses' % (count))
    print('-------------------------')
    ip_counts.sort()
    for (num, ipv) in ip_counts:
        print('IP: %s\tCount: %d' % (ipv, num))
                        

if __name__ == '__main__':
    if len(sys.argv) > 1:
        print('Invalid arguments. Proper usage is ./dextract-ipinfo.py')
    else:
        extract_ip_data()
