#!/usr/bin/python
# -*- encoding: utf-8 -*-

import urllib
import xml.etree.ElementTree as ET
import json

fqdn = 'http://localhost:8983/solr/'
uri = 'admin/cores?action=STATUS&wt=xml'

def main():
    
    data = []
    
    resp=urllib.urlopen(fqdn+uri).read()
    tree = ET.fromstring(resp)
    for lst in tree.findall("lst"):
        for lst2 in lst.findall("lst"):
            name=lst2.attrib['name'];
            core={}
            nameSplit=name.split("_",2)
            core["{#CORENAME}"]=name;
            core["{#SHARD_NAME}"]=nameSplit[1];
            core["{#REPLICA_NAME}"]=nameSplit[2];
            core["{#COLLECTION}"]=nameSplit[0];
            data.append(core)
   
    print  json.dumps({"data": data})


if __name__ == "__main__":
    main() 
