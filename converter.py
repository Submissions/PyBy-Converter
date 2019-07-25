#!/usr/bin/env python3

#### Converting Bytes to MB, GB, TB

import os
import sys

def MB(x):
    M = x / 1024 / 1024
    return M

def GB(x):
    G = MB(x) / 1024
    return G

def TB(x):
    T = GB(x) / 1024
    return T

def byte_converter(*args):
    for	i in args:
        print("This is the result for %d bytes" %i)
        print("MB", MB(i))
        print("GB", GB(i))
        print("TB", TB(i))

for bytes_in in list(map(int, sys.argv[1:])):
    byte_converter(bytes_in)
