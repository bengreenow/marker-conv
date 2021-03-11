#!/usr/bin/env python
import argparse
import sys
import csv
import codecs
import datetime

parser = argparse.ArgumentParser(
    description='Convert markers .csv file to YouTube ready timestamps')
parser.add_argument('csv', metavar='f', help='utf-16 encoded csv file from Premiere Pro', nargs='*',
                    type=argparse.FileType('r', encoding='utf-16'))
parser.add_argument("-t", '--titlecase',
                    help='Converts the resulting timestamp names to title case',
                    action='store_true')

args = parser.parse_args()
output = []
objectlist = []

for csvFile in args.csv:  # cast csv file to array
    reader = csv.reader(csvFile)
    for i, row in enumerate(reader):
        if i == 0:
            continue
        output.append(list(filter(None, row[0].split("\t"))))

for row in output:  # create objects from array

    timeString = row[1][:-3]
    name = (row[0].title() if args.titlecase else row[0])  # title case check

    objectlist.append((name, datetime.time(
        hour=int(timeString[0:2]),
        minute=int(timeString[3:5]),
        second=int(timeString[6:8]),
        microsecond=0
    )))

# Timestamps generated in objectlist

for times in objectlist:
    time = (str(times[1]) if times[1].hour != 0 else str(times[1])[3:])
    print(time, times[0])
