#!/usr/bin/python3
#06_set_config_hostname_cisco.py
#Autor: Andrés Ripoll

from ncclient import manager
from lxml import etree

nc = manager.connect(
	host = "172.20.20.2", 
	port = "830", 
	timeout = 30,
	username = "admin",
	password = "admin",
	hostkey_verify = False,
	look_for_keys = False,
	allow_agent = False
)

#Set Configurations
cfg_hostname = """
<config xmlns="urn:ietf:params:xml:ns:netconf:base:1.0">
	<native
		xmlns="http://cisco.com/ns/yang/Cisco-IOS-XE-native">
		<hostname>test1234</hostname>
	</native>
</config>
"""

reply = nc.edit_config(
	config=cfg_hostname,
	target="running",
)
print(reply)

nc.close_session()
