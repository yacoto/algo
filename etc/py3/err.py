#!/usr/bin/env python3
# coding=utf-8

from functools import reduce
import logging
logging.basicConfig(level=logging.INFO)

def str2num(s):
    return int(s)

def calc(exp):
    ss = exp.split('+')
    #ns = map(str2num, ss)
    ns = map(int, ss)
    #ns = map(lambda x:int(x), ss)
    return reduce(lambda acc, x: acc + x, ns)

def main():
    r = calc('100 + 200 + 345')
    print('100 + 200 + 345 =', r)
    r = calc('99 + 88 + 7.6')
    print('99 + 88 + 7.6 =', r)

main()

