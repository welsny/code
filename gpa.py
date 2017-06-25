#!/usr/bin/env python
# -*- coding: utf-8 -*-

import csv
import optparse

def read_cl():
    parser = optparse.OptionParser()

    parser.add_option("-f","--filename", default="grades.csv", help="file to read")
    parser.add_option("-n","--neu", default=True, action="store_false",
                      help="use standard GPA scale (default: NEU scale)")
    options, args = parser.parse_args()

    return options.filename, options.neu

def calc_gpa(filename, NEU):
    if NEU:
        SCORE = {'F':0, 'A':4, 'A-':3.667,
                'B+':3.333, 'B':3, 'B-':2.667,
                'C+':2.333, 'C':2, 'C-':1.667,
                'D+':1.333, 'D':1, 'D-':0.667}
    else:
        SCORE = {'F':0, 'A':4, 'A-':3.7,
                'B+':3.3, 'B':3, 'B-':2.7,
                'C+':2.3, 'C':2, 'C-':1.7,
                'D+':1.3, 'D':1, 'D-':0.7}

    credits = 0
    points = 0

    data = csv.DictReader(open(filename))
    for row in data:
        credits += int(row['credits'])
        points  += int(row['credits']) * SCORE[row['grade']]

    print points/credits

if __name__ == "__main__":
    fname, neu = read_cl()
    calc_gpa(fname, neu)

