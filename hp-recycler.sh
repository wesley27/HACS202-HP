#!/bin/bash
#
# *** This script should be run in the background output to a log file ***
# *** Run upon honeypot deployment, or restart if honeypots are restarted ***
#
# This script handles the recycling of all honeypot containers over
# a set period of time. It restores active honeypots to a clean,
# uncompromised backup so that they may maintain their research
# initiative and be compromised again.

# Lifecycle is 12 hours. General procedure is as follows:
# 1. Kill all MITMs
# 2. Stop container
# 3. Unmount container storage
# 4. Destroy container
# 5. Restore container from backup of base configuration ("containerid.tar")
# 6. Start container
# - Loop steps 2-6 for each honeypot
# 7. Start all MITMS

BASE_PCT_PATH="/var/lib/vz/dump/"
ctrs=("101" "102" "103" "104")

while true
do
    sleep 43200

    mitm-ssr stop all
    timestamp=$(date '+%Y-%m-%d %H:%M:%S')
    echo "$timestamp | All MITM instances have been stopped."
    timestamp=$(date '+%Y-%m-%d %H:%M:%S')
    echo "$timestamp | -"

    for ctr in "${ctrs[@]}"
    do
        pct stop $ctr > /dev/null
        timestamp=$(date '+%Y-%m-%d %H:%M:%S')
        echo "$timestamp | Honeypot container $ctr stopped."
    
        umount /media/$ctr > /dev/null
        timestamp=$(date '+%Y-%m-%d %H:%M:%S')
        echo "$timestamp | Honeypot container $ctr storage unmounted."

        pct destroy $ctr > /dev/null
        timestamp=$(date '+%Y-%m-%d %H:%M:%S')
        echo "$timestamp | Honeypot container $ctr destroyed."

        pct restore $ctr $BASE_PCT_PATH$ctr.tar --storage local-lvm > /dev/null
        timestamp=$(date '+%Y-%m-%d %H:%M:%S')
        echo "$timestamp | Honeypot container $ctr restored from base."

        pct start $ctr > /dev/null
        timestamp=$(date '+%Y-%m-%d %H:%M:%S')
        echo "$timestamp | Honeypot container $ctr started."

        timestamp=$(date '+%Y-%m-%d %H:%M:%S')
        echo "$timestamp | Honeypot container $ctr has been recycled."
        
        timestamp=$(date '+%Y-%m-%d %H:%M:%S')
        echo "$timestamp | -"
    done

    mitm-ssr start all
    timestamp=$(date '+%Y-%m-%d %H:%M:%S')
    echo "$timestamp | All MITM instances have been started."
    echo "-------------------------------------------------------"
done
