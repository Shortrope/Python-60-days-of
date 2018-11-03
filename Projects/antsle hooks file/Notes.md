# Hook File script notes

## 11/3/2018  Pair programing w William

### 1. Getting multiple iterations of the same antlet_info in the `list_of_antlets`
Our for loop process:

    read line
    add line info to dict
    append dict to list_of_antlets

if we have info for a single antlet

    antlet_name=mysql-db
    antlet_type=lxc
    antlet_ip=10.1.1.10
    host_ip=192.168.1.3
    portmap=1111:1111
    portmap=2222:2222

We were appending the dict to the list for each line of data
**BUT** The `dict` we are adding is an object reference. 
The list_of_antlets ends up with a length equal to the number of lines for that antlet.
And each element is the same object reference... the same object