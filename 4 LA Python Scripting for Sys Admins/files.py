#!/usr/bin/env python3

xmen_file = open('xmen-base.txt', 'r')

#print(xmen_file.read())
#xmen_file.seek(16)
#print(xmen_file.read())


new_xmen = open('new-xmen.txt', '+')
#print(new_xmen.read())
new_xmen.write(xmen_file.read())
print(new_xmen.read())


xmen_file.close()
new_xmen.close()