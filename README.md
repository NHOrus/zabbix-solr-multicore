# zabbix-solr-multicore for Solr version 7.5 and later
Primitive solution for SolR monitoring on Zabbix

# Change Log
1. Default response format of admin status is now json so use wt=xml 
2. Need collection name, shard name and replica name separately as Solr JMX Bean Names have changed
3. Change JMX keys according Solr Version 7

# Issues
1. Works only for Solr 7.5 (this is latest version on 2018-11-06) and later
2. Works only for Solr Cloud Setup

# Setup
1. Copy solr.conf to /etc/zabbix/zabbix_agentd.d/ on solr host
2. Copy Solr-pypoll.py to /usr/local/zabbix/ or to any other directory and provide its path in solr.conf on solr host
3. Import zbx-zabbix-solr-multicore.xml to zabbix 
4. Add template to SOLR_JMX_V7.5 to solr host

Please comment if you find any more issues.

Thank you to original author @ https://github.com/Hackuracy
