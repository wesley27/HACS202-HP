import yaml

class Honeypot:
    def __init__(self, hp_id = None, ip = None, c_id = None, c_ip = None, mitm_p = None):
        self.hp_id = hp_id
        self.ip = ip
        self.c_id = c_id
        self.c_ip = c_ip
        self.mitm_p = mitm_p

def load_hpData():
    with open('.conf.yml', 'r') as ymlfile:
        config = yaml.load(ymlfile)

    honeypot_list = []
    for key in config['publicIP']:
        hp_id = key[2:]
        hp_ip = config['publicIP'][key]
        c_id = config['containerID'][key]
        c_ip = config['containerIP'][key]
        mitm_p = config['mitmPort'][key]

        hp = Honeypot(hp_id, hp_ip, c_id, c_ip, mitm_p)
        honeypot_list.append(hp)
    return honeypot_list
