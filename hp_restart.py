#!/usr/bin/env python
import subprocess
import sys

def restart_hp(hp):
    if hp == 'all':
        restart_hp(1)
        restart_hp(2)
        restart_hp(3)
        restart_hp(4)
    elif hp == '1':
    elif hp == '2':
    elif hp == '3':
    else:

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print('Invalid number of arguments. Proper usage is ./hp-restart <honeypot #>')
    elif sys.argv[1] not in ['1', '2', '3', '4', 'all']:
        print('Invalid argument used. Proper usage is ./hp-restart <honeypot #>')
    else:
        restart_hp(sys.argv[1])
