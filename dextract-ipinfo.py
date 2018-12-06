#!/usr/bin/env python
import subprocess
import sys
import os
import re
from urllib2 import urlopen, HTTPError
import json
import csv
import unicodedata


"""
This script handles the processing of attacker session files to obtain
IP address information and statistics. It outputs this data to a csv
file that can be found at ./ipdata.csv. 

The directory ./processed must exist before running this script. It moves
processed session files into the ./processed folder. It also outputs a
frequency chart to ./processed/frequencies.txt
chart for all IPs found.

Proper usage:
./dextract-ipinfo.py
"""

STR_ATK_IP = 'Attacker IP Address:'
LN_END = '\n'

def extract_ip_data():
    session_pattern = re.compile('^[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}')
    csvout = open('ipdata.csv', 'wb')
    filewriter = csv.writer(csvout, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL)
    filewriter.writerow(['IP_address', 'city', 'country', 'IP_org'])
    ip_counts = []
    count = 0
    limit_met = 0
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
                        try:
                            response = urlopen(STR_IP_LKUP)
                            ipdata = json.load(response)
                            if 'city' not in ipdata:
                                continue
                            city = ipdata['city']
                            country = ipdata['country']
                            org = ipdata['org']
                            print('ip: %s \tcity: %s \tcountry: %s \torg: %s' % (ip, city, country, org))
                            try:
                                filewriter.writerow([ip, city, country, org])
                            except UnicodeEncodeError as e:
                                city = unicodedata.normalize('NFKD', city).encode('ascii', 'ignore')
                                country = unicodedata.normalize('NFKD', country).encode('ascii', 'ignore')
                                org = unicodedata.normalize('NFKD', org).encode('ascii', 'ignore')
                                filewriter.writerow([ip, city, country, org])
                            count += 1
                        except HTTPError as e:
                            limit_met = 1
                            break
                f.close()
                CMD_MV = 'mv %s processed' % filename
                os.system(CMD_MV)
                if limit_met != 0:
                    break
    csvout.close()

    freq_file_path = 'processed/frequencies.txt'
    with open(freq_file_path, 'a+') as f:
        for line in f:
            if '------' in line or 'Processed' in line:
                continue

            vals = line.split()
            rIP = vals[1]
            rCount = vals[3]
            rFound = 0
            count += int(rCount)

            # add pre-existing ip stats to list that was just generated
            for (onum, ipv) in ip_counts:
                if ipv == rIP:
                    ip_counts[ip_counts.index((onum, ipv))] = (onum + int(rCount), ipv)
                    rFound = 1
                    break
            if rFound == 0:
                ip_counts.append((rCount, rIP))
        f.close()
    
    with open(freq_file_path, 'w') as f:
        # rewrite file from beginning
        f.write('-------------------------%s' % LN_END)
        f.write('Processed %d IP addresses%s' % (count, LN_END))
        f.write('-------------------------%s' % LN_END)

        ip_counts.sort()
        for (num, ipv) in ip_counts:
            f.write('IP: %s\tCount: %d%s' % (ipv, num, LN_END))
        f.truncate()
        f.close()
                        

if __name__ == '__main__':
    if len(sys.argv) > 1:
        print('Invalid arguments. Proper usage is ./dextract-ipinfo.py')
    else:
        extract_ip_data()
