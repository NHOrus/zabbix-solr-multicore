#!/usr/bin/python
# -*- encoding: utf-8 -*-

import urllib
import xml.etree.ElementTree as ET
import json
import re

fqdn = 'http://localhost:8983/solr/'
uri = 'admin/cores?action=STATUS&wt=xml'

def main():
    
    data = []
    
    resp=urllib.urlopen(fqdn+uri).read()
    tree = ET.fromstring(resp)
    for lst in tree.findall("lst"):
        for lst2 in lst.findall("lst"):
            name=lst2.attrib['name'];
            nameSplit = re.match('^([^_]+)_(shard.*)_(replica\w+)$',name)
            core={}
            core["{#CORENAME}"]=name;
            core["{#COLLECTION}"]=nameSplit.group(1);
            core["{#SHARD_NAME}"]=nameSplit.group(2);
            core["{#REPLICA_NAME}"]=nameSplit.group(3);
            data.append(core)
   
    print  json.dumps({"data": data})


if __name__ == "__main__":
    main() 
