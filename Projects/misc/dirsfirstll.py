#!/usr/bin/python3

from subprocess import Popen, PIPE

dlist = Popen(['ls', '-l'], stdout=PIPE)
dirs = []
files = []

def showlist():
    for item in dlist.stdout:
        line = item.decode().strip()
        if line.startswith('total'):
            continue
        elif line.startswith('d'):
            dirs.append('{0}/'.format(line))
        else:
            files.append( '{0}'.format(line))

    for item in dirs + files:
        print(item)

if __name__ == "__main__":
    showlist()

