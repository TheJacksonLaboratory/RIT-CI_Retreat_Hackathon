#!/bin/python

import io
with io.open("20140927","r") as f:

c = f.read()
lines = c.split("\n")

newlist = [ l.split() for i in lines ]
yetanothernewlist = [ mylist for mylist in newlist if mylist ]
items = [data[1:] for data in yetanothernewlist]
record_list = [ { val.split("=")[0]:val.split("=")[1] for val in sublist } for sublist in items]
print(record_list)
