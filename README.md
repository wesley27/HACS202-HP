# HACS202-HP
This repository is a collection of scripts, tools, functions, and research used to conduct honeypot research for HACS202.

## Repository Contents
[Heatmap Generation Script](mapgen2.py)\
[Honeypot MITM Restart Script](mitm-ssr)\
[Honeypot Recycling Script](hp-recycler.sh)\
[Honeypot Configuration Loader](honeypot.py)\
[Honeypot Individual Command Extractor](hpcmd-ex.sh)\
[IP Information Extractor](dextract-ipinfo.py)\
[IP CSV File Corrector](ip-csv-corrector.py)\
[Session Information Extractor](dextract-sessioninfo.py)\
[Session Type Statistics Calculator](session-calculator.sh)\
[Session Unzipper](session-extractor.py)\
[Script->Path CMD Loader](cmdloader.sh)

### Configuration Details
Scripts requiring honeypot information (ips, containers, ports, etc) obtain any required details from a locally stored configuration (.conf.yml). This file is ommitted from the public online repository due to the sensitive nature of its contents.

Scripts can use the following to easily access honeypot configuration data:
```
from honeypot import *
honeypots = []
honeypots = load_hpData()

# prints the data in honeypot 1
for hps in honeypots:
    if hps.hp_id == '1':
        hp = hps
        break

print(hp.ip)
```

The following is a template of **.conf.yml**, with sensitive information removed:
```
#.conf.yml base template

publicIP:
    hp1: <ip1>
    hp2: <ip2>
    hp3: <ip3>
    hp4: <ip4>

containerID:
    hp1: <cid1>
    hp2: <cid2>
    hp3: <cid3>
    hp4: <cid4>

mitmPort:
    hp1: <port1>
    hp2: <port2>
    hp3: <port3>
    hp4: <port4>

containerIP:
    gw: <gw ip>
    hp1: <hp1 ip>
    hp2: <hp2 ip>
    hp3: <hp3 ip>
    hp4: <hp4 ip>
```

### HeatMap Generation
The heatmap generator script requires a CSV file with the latitude and longitude of each geolocated IP address. It also requires a Google API key.
