# Files

## open()
Opens a file  
- file: path to file (required)
- mode: read/write/append, binary/text
- encoding: text encoding

Files are a series of bytes  
Files can be opened in binary or text mode  
Binary mode, data is read as `bytes` objects  
Binary mode data is the raw data in the file.  
Text mode: data is read as strings  
Text mode: data has been `decoded` from the specified encoding  
Text mode uses pythons _universal newlines_  

Getting the encoding right is crucial!  
No guarante the encoding will be the same on two different systems.
If not specified, python will use the system default encoding.

    import sys
    sys.getdefaultencoding()

(Get a list of standard encodings)[http://docs.python.org/3/library/codecs.html#standard-encodings]

### f.write()

    f = open('filename.txt', mode='wt', encoding='utf-8')
    help(f)

- mode must include an 'r', 'w' or 'a' 
    - r, w, a, x, b, t, +, U

Write to the file  
Will return the number of 'code points' (chars) written  

    f.write("Mindset, The new psychology of success\n")
    f.writelines(["Mindset, The new psychology of success\n",
                  "Through clever research studies and engaging writing.\n",
                  "How we learn and which paths we take in life.\n"])

Close the file when done

    f.close()



### f.read()

    g.open('wasteland.txt', mode='rt', encoding='utf-8')

Read all contents of the file
This will render the entire file as a single line string - new lines as '\n' ??

    g.read()

Read, you can specify the number of chars

    g.read(32)

Set the pointer back to the beginning

    g.seek(0)

Other methods

    g.readline()    # returns the next line
    g.seek(0)
    g.readlines()   # returns a list of lines

### Iterate
A file object is iterable

    for line in f:
        sys.stdout.write(line)

## try...finally
Make sure the file closes if something goes awry

    try:
        f = open('filename.txt', mode='wt', encoding='utf-8')
        # do something
    finally:
        f.close()

## with-block
Resource cleanup w context-managers  
`open()` returns a context-manager  
No longer need to call `close()` 

    with open(filename, 'rt', 'utf-8') as f:
        # do stuff



## File like objects
loosely-defined set of behaviors for things that act like files


