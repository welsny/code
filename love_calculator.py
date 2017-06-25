#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
from pyllist import sllist

"""
Python implementation of the early 2000's hit classic www.LoveCalculator.com
"""

def count(name1, name2):
    """
    Produces a 5-digit number which represents the letters in the two names.

    Args:
        name1 (string): the name of the first person
        name2 (string): the name of the second person
    Returns:
        A linked list of integers containing the count of characters in the names.
    """
    letters = (name1+name2).lower()

    counts = {char: letters.count(char) for char in 'loves'}
    result = [counts[char] for char in 'loves']
    return sllist(result)

def step(sll):
    """
    Runs a single iteration of the merge step of LoveAlgorithm.
    """
    for node in sll.iternodes():
        try:
            node.value += node.next()
            if node.value >= 10:
                sll.insertbefore(node, node.value/10)
                node.value %= 10
        except TypeError:
            'reached end of sllist'
            sll.popright()

def add(letters):
    """
    Runs the merge steps of LoveAlgorithm on a sllist until we reach a final result.

    Runs the loveAlgorithm to reduce a length-5 singly-linked list to length <= 2.

    Returns a 2-digit integer. Returns 1 if an infinite loop is detected.
    """

    seen = set()
    while len(letters) > 2:
        # Cast SLL to string since we cannot hash a mutable object:
        if str(letters) in seen:
            return 1
        seen.add(str(letters))

        step(letters)

    if len(letters) == 2:
        return 10*letters[0] + letters[1]
    return letters[0]

def get_text(percent):
    score = percent/10
    return { 9: "Extremely favorable!",
             8: "Very favorable!",
             7: "Favorable!",
             6: "Slightly favorable",
             5: "Decent",
             4: "slightly unfavorable",
             3: "Unfavorable"
           }.get(score, "Very unfavorable")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Please enter two names - ")
        sys.exit()

    counts = count(sys.argv[1], sys.argv[2])
    result = add(counts)

    print('\nChance of Successful Relationship: {0}% - {1}\n'.format(str(result), get_text(result)))

