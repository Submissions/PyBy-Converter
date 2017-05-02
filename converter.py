#!/usr/bin/python

#### Converting Bytes to MB, GB, TB

import os
import sys

def MB(x):
    M = float(x) / float(1024) / float(1024)
    return M

def GB(x):
    G = float(MB(x)) / float(1024)
    return G

def TB(x):
    T = float(GB(x)) / float(1024)
    return T

def byte_converter(*args):
    for	i in args:
        print("This is the result for %d bytes" %i)
        print("MB", MB(i))
        print("GB", GB(i))
        print("TB", TB(i))

for bytes_in in list(map(int, sys.argv[1:])):
    byte_converter(bytes_in)
