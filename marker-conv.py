#!/usr/bin/env python
import argparse
import sys
import csv
import codecs

output = []

with codecs.open('test.csv', 'r', 'utf-16') as csvFile:
    reader = csv.reader(csvFile)
    for i, row in enumerate(reader):
        if i == 0:
            continue  # ignore column headers
        output.append(list(filter(None, row[0].split("\t"))))

timestamps = []

for row in output:
    ts = row[1][3:-3] + ' ' + row[0]
    timestamps.append(ts)
    print(ts)
