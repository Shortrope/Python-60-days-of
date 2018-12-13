# Environment Variables
import os
os.environ['HOME']
os.environ['STAGE']
os.getenv(key, default=prod)

    app.py
    STAGE=dev app.py


# Working w Files

with open('file.txt', 'r') as f:
with open('file.txt', 'w') as f:
with open('file.txt', 'a') as f:
'b' binary
't' text
'+' reading and writing


f.read()        
f.seek(0)       # resets the cursor to the begining of the file
f.readlines()
f.write(str)


