#!/bin/python
'''
This script parses every log file in the Helix Log Directory and prints the corresponding JSON
'''
import io, glob, os
path = 'helixlogs/'
for mylogfile in glob.glob(os.path.join(path, '*')):
    print("\n", mylogfile)
    with open(mylogfile, "r") as f:
        text = f.read()
        lines = text.split("\n")
        newlist = [ l.split() for l in lines ]
        yetanothernewlist = [ mylist for mylist in newlist if mylist ]
        items = [data[1:] for data in yetanothernewlist]
        record_list = [ { val.split("=")[0]:val.split("=")[1] for val in sublist } for sublist in items]
        print(record_list)

#with io.open("file","w") as output:
