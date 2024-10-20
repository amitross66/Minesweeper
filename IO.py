"""
IO for the program, to allow for decoupling (in hopes of creating a GUI one day)
"""

from scanf import scanf

def read(__prompt):
    return input(__prompt)

def readf(format, s=None, collapseWhitespace=True):
    return scanf(format, s, collapseWhitespace)

def write(__str):
    print(__str)