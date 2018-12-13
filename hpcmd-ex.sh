#!/bin/bash

cat session_data.csv | grep "%101%" | cut -d "%" -f 5 | grep "\['" | tr -d "[']" > hp101_cmds.txt

cat session_data.csv | grep "%102%" | cut -d "%" -f 5 | grep "\['" | tr -d "[']" > hp102_cmds.txt

cat session_data.csv | grep "%103%" | cut -d "%" -f 5 | grep "\['" | tr -d "[']" > hp103_cmds.txt

cat session_data.csv | grep "%104%" | cut -d "%" -f 5 | grep "\['" | tr -d "[']" > hp104_cmds.txt
