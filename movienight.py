#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
NU CSA Events Committee
Movie Night 2015
'''

titles = {1: 'Crouching Tiger, Hidden Dragon',
          2: 'Shaolin Soccer',
          3: '那些年 Apple of my Eye',
          4: 'Infernal Affairs'}

votes = {title: 0 for title in titles.values()}

while True:
    print("\nMovie Choices \n\n")

    for key, title in titles.items():
        print("%s: %s\n" % (key, title))

    try:
        x = raw_input('Cast your vote: ')
        if x == 'DONE': break
        x = int(x)
    except:
        pass

    if x in titles.keys():
        t = titles[x]
        votes[t] += 1
        print('\nThank you for your vote! (%s)' % t)
    else:
        print("\nInvalid input: (%s). Please try again: " % x)

print("\nFINAL TALLY: \n")

for title, count in votes.items():
    print title,':', count
