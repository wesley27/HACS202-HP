#!/usr/bin/env python
import subprocess
import sys
import yaml

honeypots = []

class Honeypot:
    def __init__(self, hp_id = None, ip = None, c_id = None, c_ip = None, mitm_p = None):
        self.hp_id = hp_id
        self.ip = ip
        self.c_id = c_id
        self.c_ip = c_ip
        self.mitm_p = mitm_p

    def hp_id(self):
        return self.hp_id

    def ip(self):
        return self.ip

    def c_id(self):
        return self.c_id

    def c_ip(self):
        return self.c_ip

    def mitm_p(self):
        return self.mitm_p

def load_hpData(config):
    for key in config['publicIP']:
        hp_id = key[2:]
        hp_ip = config['publicIP'][key]
        c_id = config['containerID'][key]
        c_ip = config['containerIP'][key]
        mitm_p = config['mitimPort'][key]

        hp = Honeypot(hp_id, hp_ip, c_id, c_ip, mitm_p)
        honeypots.append(hp)

def restart_hp(hp_id, config):
    if hp_id == 'all':
        print('> all <')
        #restart_hp(1)
        #restart_hp(2)
        #restart_hp(3)
        #restart_hp(4)
    elif hp_id == '1':            
        out = subprocess.check_output('ps aux | grep mitm')
    elif hp_id == '2':
        out = subprocess.check_output('ps aux | grep mitm')
    elif hp_id == '3':
        out = subprocess.check_output('ps aux | grep mim')
    else:
        out = subprocess.check_output('ps aux | grep mitm')

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
