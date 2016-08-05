#!/usr/bin/env python
# -*- coding: utf-8 -*-

SCORE = {'A':4,
        'A-':3.667,
        'B+':3.333,
         'B':3,
        'B-':2.667,
        'C+':2.333,
         'C':2,
        'C-':1.667,
        'D+':1.333,
         'D':1,
        'D-':0.667,
         'F':0}

data = open('grades').read()
raw = data.split('\n')[1:-1]

credits = [int(row.split(',')[0]) for row in raw]
points = [SCORE[row.split(',')[1]] for row in raw]

total_credits = sum(credits)
total_points  = sum(c*p for (c,p) in zip(credits, points))

print total_points / total_credits

