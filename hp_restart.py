#!/usr/bin/env python
import subprocess
import os
import sys
import yaml

MITM_FILE = '/root/MITM/mitm/index.js'
MITM_LOG_PATH = '~/mitm_logs/mitm'
honeypots = []

class Honeypot:
    def __init__(self, hp_id = None, ip = None, c_id = None, c_ip = None, mitm_p = None):
        self.hp_id = hp_id
        self.ip = ip
        self.c_id = c_id
        self.c_ip = c_ip
        self.mitm_p = mitm_p

def load_hpData(config):
    for key in config['publicIP']:
        hp_id = key[2:]
        hp_ip = config['publicIP'][key]
        c_id = config['containerID'][key]
        c_ip = config['containerIP'][key]
        mitm_p = config['mitmPort'][key]

        hp = Honeypot(hp_id, hp_ip, c_id, c_ip, mitm_p)
        honeypots.append(hp)

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
        with open('.conf.yml', 'r') as ymlfile:
            cfg = yaml.load(ymlfile)
        load_hpData(cfg)
        restart_hp(sys.argv[1])
