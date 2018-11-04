#!/usr/bin/python3
from pprint import pprint as pp

#hooks_conf_path = "/etc/libvirt/hooks/hooks.conf"
hooks_conf_path = "/mnt/e/_Projects/100/100-days-of-python/Projects/antsle hooks file/hooks.conf"

def clean_conf_data(hooks_conf_path):
    cleaned_data = []
    
    with open(hooks_conf_path, 'r') as f:
        for line in f:
            if line[:1] != "#":
                if line[:1] != "\n":
                    k, _, v = line.partition('=')
                    cleaned_data.extend(["{0}={1}".format(k,v).strip()])
    return cleaned_data

#print(get_antlet_data(hooks_conf_path))

def get_antlet_data(cleaned_data):
    list_of_antlets = []
    antlet_info = dict()

    for line in cleaned_data:
        if "antlet_name" in line:

            if len(antlet_info) != 0:
                list_of_antlets.append(antlet_info)

            antlet_info = dict()
            k, _, v = line.partition('=')
            antlet_info["antlet_name"] = v

        else:
            k, _, v = line.partition('=')
            if "portmap" not in line:
                antlet_info[k] = v
            else:
                hostport, _, antletport = v.partition(':')
                if "hostports" not in antlet_info:
                    antlet_info["hostports"] = "'{}' ".format(hostport)
                    antlet_info["antletports"] = "'{}' ".format(antletport)
                else:
                    antlet_info["hostports"] += "'{}' ".format(hostport)
                    antlet_info["antletports"] += "'{}' ".format(antletport)

    list_of_antlets.append(antlet_info)

    return list_of_antlets

pp(get_antlet_data(clean_conf_data(hooks_conf_path)))
