# HACS202-HP
This repository is a collection of scripts, tools, functions, and research used to conduct honeypot research for HACS202.

## Repository Contents
[Honeypot MITM Restart Script](hp_restart.py)

### Configuration Details
Scripts requiring honeypot information (ips, containers, ports, etc) obtain any reuqired details from a locally stored configuration (.conf.yml). This file is ommitted from the public online repository due to the sensitive nature of its contents.

The following is a template of **.conf.yml**, with sensitive information removed.
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
