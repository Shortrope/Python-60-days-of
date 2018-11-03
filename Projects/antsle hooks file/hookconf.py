#!/usr/bin/python3
from pprint import pprint as pp

#hook_conf = "/etc/libvirt/hooks/hooks.conf"
hook_conf = "/mnt/e/_Projects/100/100-days-of-python/Projects/antsle hooks file/hooks.conf"

def clean_conf_data(hook_conf):
    open_case_statement = "case $antlet_name in"
    close_case_statement = """*)
  echo "`date` hook/${antlet_type} antlet $antlet_name No ports configured!" >>/var/log/libvirt/hook.log
  ;;
esac"""
    cleaned_data = []
    
    # read in conf file
    with open(hook_conf, 'r') as f:
        for line in f:
            if line[:1] != "#":
                if line[:1] != "\n":
                    k, _, v = line.partition('=')
                    cleaned_data.extend(["{0}={1}".format(k,v).strip()])
    return cleaned_data

#print(get_antlet_data(hook_conf))

def get_antlet_data(cleaned_data):
    list_of_antlets = []
    antlet_info = dict()

    for line in cleaned_data:
        if "antlet_name" in line:
            antlet_info = dict()
            k, _, v = line.partition('=')
            antlet_info["antlet_name"] = v
            print(antlet_info)

        elif "antlet_type" in line:
            antlet_info["antlet_type"] = line.partition('=')[2]
            print(antlet_info)

        elif "antlet_ip" in line:
            antlet_info["antlet_ip"] = line.partition('=')[2]
            print(antlet_info)

        elif "host_ip" in line:
            antlet_info["host_ip"] = line.partition('=')[2]
            print(antlet_info)

        elif "portmap" in line:
            hostport = line.partition('=')[2].partition(':')[0]
            antletport = line.partition('=')[2].partition(':')[2]
            if "hostports" not in antlet_info:
                antlet_info["hostports"] = "'{0}' ".format(hostport)
                antlet_info["antletports"] = "'{0}' ".format(antletport)
            else:
                antlet_info["hostports"] += "'{0}' ".format(hostport)
                antlet_info["antletports"] += "'{0}' ".format(antletport)
            print(antlet_info)

        else:
            print("Warning Will Robinson: can't create dict!")

        list_of_antlets.append(antlet_info)

    pp(list_of_antlets)

get_antlet_data(clean_conf_data(hook_conf))






#            m = re.search('^#', line)