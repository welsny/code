#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import pandas as pd

class Bowl():
    def __init__(self):
        self.menu = pd.read_csv('qdoba.csv')

def main():
    qd = pd.read_csv("qdoba.csv", index_col=0)
    print(qd.sum())
    print(qd.sum() - qd.loc['Brown Rice'] + qd.loc['Chicken'])
    print(qd.sum() - qd.loc['Brown Rice'] + qd.loc['Chicken'] + qd.loc['Black Beans'])
    print(qd.sum() - qd.loc['Brown Rice'] + qd.loc['Black Beans'])

if __name__ == '__main__':
    main()

