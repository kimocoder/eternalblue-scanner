#!/usr/bin/env python3

import sys

with open('/usr/local/share/Eternal_Scanner/vuln.txt','r') as file:
    with open('assets/ip.txt', 'w') as files:
        # starts from 2nd line
        file.readline()
        file.readline()

        lines = file.readlines()
        ips = []
        for i in lines:
            a = i.strip('\n').split(':')[0]
            ips.append(a)
            files.write(a+"\n")