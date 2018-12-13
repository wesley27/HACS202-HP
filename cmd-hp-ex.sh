#!/bin/bash

cat session_data.csv | grep "%101%" | cut -d "%" -f 5 | grep "\['" | tr -d "[']" > cmds_101.txt

cat session_data.csv | grep "%102%" | cut -d "%" -f 5 | grep "\['" | tr -d "[']" > cmds_102.txt

cat session_data.csv | grep "%103%" | cut -d "%" -f 5 | grep "\['" | tr -d "[']" > cmds_103.txt

cat session_data.csv | grep "%104%" | cut -d "%" -f 5 | grep "\['" | tr -d "[']" > cmds_104.txt
