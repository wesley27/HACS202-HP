import yaml

"""
This class defines a data structure for storing crtical
honeypot configuration data. A defined "Honeypot" consists
of the following values:

hp_id - the honeypot ID
ip    - the public IP of the honeypot
c_id  - the container id of the honeypot
c_ip  - the private IP of the container
mitm_p  - the port of the honeypot's MITM (man in the middle)

Scripts requiring this information can obtain a list of
Honeypot data structures by importing this file and 
calling load_hpData(). This function requires that a
.conf.yml file exists in the format specified in the README.
"""

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
