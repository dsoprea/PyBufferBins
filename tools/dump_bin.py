#!/usr/bin/python

from sys import argv, exit

from pybufferbins.bins import Bins

if len(argv) < 4:
    print("Please provide <module> <class name> <file to read>")
    print
    exit()

(_, module_name, class_name, file_path) = argv

m = __import__(module_name, fromlist=[class_name])
cls = getattr(m, class_name)

for item in Bins.bin_foreach(cls, file_path):
    print(item)

