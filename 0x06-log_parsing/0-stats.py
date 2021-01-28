#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
Created on Fri Dec  11 8:24:21 2020

@author: Robinson Montes
"""
import sys


total_size = 0
count = 0
status_codes = {'200': 0, '301': 0, '400': 0, '401': 0, '403': 0, '404': 0,
               '405': 0, '500': 0}

try:
    for line in sys.stdin:
        words = line.split(" ")
        if len(words) > 2:
            size = words[-1]
            status = words[-2]
            if status in status_codes:
                status_codes[status] += 1
            total_size += int(size)
            count += 1
        if count == 10:
            print("File size: {:d}".format(total_size))
            for k, v in status_codes.items:
                if v != 0:
                    print("{:}: {:d}".format(k, v))
            count = 0
except Exception:
    pass
finally:
    print("File size: {:d}".format(total_size))
    for k, v in status_codes.items:
        if v != 0:
            print("{:}: {:d}".format(k, v))
