#!/usr/bin/env python
import subprocess
import os
import sys

from honeypot import *

MITM_FILE = '/root/MITM/mitm/index.js'
MITM_LOG_PATH = '~/mitm_logs/mitm'
honeypots = []

def restart_hp(hp_id):
    hp = None
    for hps in honeypots:
        if hps.hp_id == hp_id:
            hp = hps
            break
    if hp is None and hp_id != 'all':
        print('Failed to locate honeypot ' + hp_id + '.')
        exit()

    if hp_id == 'all':
        restart_hp('1')
        restart_hp('2')
        restart_hp('3')
        restart_hp('4')
    else:
        cmd_ps = 'ps aux | grep mitm | grep %s | grep -v \'/bin/sh\' | awk \'{print $2}\'' % hp.c_id
        cmd_kl = 'kill '
        cmd_nh = 'nohup node %s HACS202_D %s %s %s > %s%s.log 2>&1&' % (MITM_FILE, hp.mitm_p, hp.c_ip, hp.c_id, MITM_LOG_PATH, hp.hp_id)

        pid = subprocess.check_output(cmd_ps, shell=True, stderr=subprocess.STDOUT).strip()
        os.system(cmd_kl + pid)
        os.system(cmd_nh)

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print('Invalid number of arguments. Proper usage is ./hp-restart <honeypot #>')
    elif sys.argv[1] not in ['1', '2', '3', '4', 'all']:
        print('Invalid argument used. Proper usage is ./hp-restart <honeypot #>')
    else:
        honeypots = load_hpData()
        restart_hp(sys.argv[1])
