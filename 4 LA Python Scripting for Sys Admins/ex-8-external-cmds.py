#!/usr/bin/env python3

from subprocess import Popen, PIPE
import argparse
import os
import sys

parser = argparse.ArgumentParser()
parser.add_argument("port_number", help="Port number to search for")

args = parser.parse_args()

port_argument = "-i4TCP:{}".format(args.port_number)
lsof_result = Popen(['lsof', '-n', port_argument], stdout=PIPE)

pid = None
for bytes in lsof_result.stdout:
    line = bytes.decode().strip()
    if 'LISTEN' in line:
        pid = int(line.split()[1])

if pid:
    result = os.kill(pid, 9)
else:
    print('Nothing LISTENing on port {}'.format(args.port_number))
    sys.exit(1)    