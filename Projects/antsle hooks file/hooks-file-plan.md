# Create Hooks file for antsle

## Get Port Forwarding Info
Use command line arguments to input info

### Inputs
- antlet name
- antlet listen ports
- host listen ports

## Auto Input
- Host IP
- antlet IP
- antlet type

## Checks
- Valid antlet name
- Host ports already used

---

## Help
    # create-hook-file --help  
    Usage: create-hook-file [options] antlet_name portmap1 [portmap2 portmapN]
    portmap can be in the form of a single port number
      80                    Both the host and antlet port are the same
    or in the form host_port:antlet_port useing a semicolon separator
      8080:80               Differing host and antlet port numbers

    Options:
      -h,  --help           Show this help message
      -v,  --verbose        Display feedback for each step processed
