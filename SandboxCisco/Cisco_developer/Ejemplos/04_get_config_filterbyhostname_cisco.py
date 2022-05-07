#!/usr/bin/python3
#04_get_config_filterbyhostname_cisco.py
#Autor: Andrés Ripoll

from ncclient import manager

nc = manager.connect(
	host = "sandbox-iosxe-latest-1.cisco.com", 
	port = "830", 
	timeout = 30,
	username = "developer",
	password = "C1sco12345",
	hostkey_verify = False,
	look_for_keys = False,
	allow_agent = False
)

#Get Configurations
FILTER = """
<native
	xmlns="http://cisco.com/ns/yang/Cisco-IOS-XE-native">
	<hostname></hostname>
</native>
"""
print(nc.get_config(source="running", filter=("subtree", FILTER)))

nc.close_session()