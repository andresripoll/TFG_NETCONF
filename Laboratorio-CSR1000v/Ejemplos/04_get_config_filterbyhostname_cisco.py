#!/usr/bin/python3
#04_get_config_filterbyhostname_cisco.py
#Autor: Andrés Ripoll

from ncclient import manager

nc = manager.connect(
	host = "172.20.20.3", 
	port = "830", 
	timeout = 30,
	username = "admin",
	password = "admin",
	hostkey_verify = False,
	look_for_keys = False,
	allow_agent = False
)

#Get Configurations
hostname = """
<native
	xmlns="http://cisco.com/ns/yang/Cisco-IOS-XE-native">
	<hostname></hostname>
</native>
"""

print(nc.get_config(source="running", filter=("subtree", hostname)))

nc.close_session()
