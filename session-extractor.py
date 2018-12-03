#!/usr/bin/env python
import os
import subprocess
import sys

"""
This script handles the automatic decompression of attacker session files.
It moves all corrupted (g-unzippable) files into the /attacker_session/temp
folder as they are mostly useless.

Proper usage:
./session-extractor.py
"""

CMD_LS = 'ls | grep \'.gz\' | wc -l'
CMD_EXTRACT = 'gunzip *.gz'

def extract_files():
    ls = subprocess.check_output(CMD_LS, shell=True, stderr=subprocess.STDOUT)
    for x in range(0, int(ls.split('\n')[0])):
        try:
            result = subprocess.check_output(CMD_EXTRACT, shell=True, stderr=subprocess.STDOUT)
        
            if 'No such file or directory' in result:
                print('Unable to find any files to extract')
                exit(0)
            elif 'unexpected end of file' in result:
                res = result.split(': ')
                CMD_MV = 'mv %s temp' % (res[1])
                os.system(CMD_MV)
        
        except subprocess.CalledProcessError as e:
            if 'No such file or directory' in e.output:
                print('Unable to find any files to extract')
                exit(0)
            elif 'unexpected end of file' in e.output:
                res = e.output.split(': ')
                CMD_MV = 'mv %s temp' % (res[1])
                os.system(CMD_MV)            

if __name__ == '__main__':
    if len(sys.argv) > 1:
        print('Invalid arguments. Proper usage is ./session-extractor.py')
    else:
        extract_files()
