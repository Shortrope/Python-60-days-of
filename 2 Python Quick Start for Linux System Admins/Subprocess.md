# Subprocess

## Strings vs Bytes
- Strings: 
    - are a sequence of _Unicode Characters_  
Can support a wide range of _Character Sets_  
- Bytes:
    - Linux text file or stream: is a sequence of bytes (ascii)
- encode() decode()
    - Methods to convert between bytes and strings

### encode()
- 'encodes' a string into bytes
### decode()
- 'decodes' bytes into a string - make it readable


## Execute programs from a Python Script

`from subprocess import Popen`  

 Popen("ls")
 Popen(["ls", "-l"])
 Popen("ls -l /etc/init.d/net.*", shell=True)


    from subprocess import Popen, PIPE
    
        lister = Popen(["ls", "-l"], stdout=PIPE)
        for bytes in lister.stdout
            line = bytes.decode()
            if line.startswith("total"):
                continue
            splitline = line.split()
            if int(splitline[4]) > 10000:
                print(splitline[8])

