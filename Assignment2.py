#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan 20 01:29:29 2020
Program to read apache logs and write to csv with connection ip and timestamp
@author: A00433151
"""

import re
import csv

list_new=[]
input_file=open("./apache_log.txt")              # Change this path to your working directory with data file
for line in input_file.readlines():
    pattern1 = r'^\b(?:[0-9]{1,3}\.){3}[0-9]{1,3}\b'
    pattern2 = r'[\d]{1,2}/[ADFJMNOS|adfjmnos]\w*/[\d]{4}:[\d]{1,2}:[\d]{1,2}:[\d]{1,2}[\s][+|-][\d]{4}'
    ip = re.findall(pattern1, line)
    timestamp = re.findall(pattern2, line)
    ip_corrected = str(ip)[2:-2]                                            # Removed square brackets and quotes at start and end of list 
    timestamp_corrected = str(timestamp)[2:-2]                              # Removed square brackets and quotes at start and end of list 
    list_new.append([ip_corrected, timestamp_corrected])
with open("./apache_log_export.csv", 'w', newline='') as export_file:         # Change this path to your working directory where the export file is saved
    for i in list_new:
        writer = csv.writer(export_file)
        writer.writerow(i)

