#!/bin/bash
echo "Calculating session data for $@"
echo "101 non-empty sessions:"
cat $@ | grep "%101%" | cut -d "%" -f 5 | grep "\['" | wc -l
echo "101 total sessions:"
cat $@ | grep "%101%" | wc -l
echo ""
echo "102 non-empty sessions:"
cat $@ | grep "%102%" | cut -d "%" -f 5 | grep "\['" | wc -l
echo "102 total sessions:"
cat $@ | grep "%102%" | wc -l
echo ""
echo "103 non-empty sessions:"
cat $@ | grep "%103%" | cut -d "%" -f 5 | grep "\['" | wc -l
echo "103 total sessions:"
cat $@ | grep "%103%" | wc -l
echo ""
echo "104 non-empty sessions:"
cat $@ | grep "%104%" | cut -d "%" -f 5 | grep "\['" | wc -l
echo "104 total sessions:"
cat $@ | grep "%104%" | wc -l
