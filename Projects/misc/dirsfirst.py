#!/usr/bin/python3
import os

for dpath, dnames, fnames in os.walk(os.getcwd()):
  for dirname in dnames:
    print(dirname + '/')

  print()

  for fname in fnames:
    print(fname)
  break


