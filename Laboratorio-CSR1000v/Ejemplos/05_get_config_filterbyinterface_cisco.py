#!/usr/bin/python3
#05_get_config_filterbyinterface_cisco.py
#Autor: Andrés Ripoll

from ncclient import manager

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

#Get Configurations
Interface_eth1 = """
<interfaces
	xmlns="urn:ietf:params:xml:ns:yang:ietf-interfaces">
	<interface>
		<name>GigabitEthernet1</name>
	</interface>
</interfaces>
"""

print(nc.get_config(source="running", filter=("subtree", Interface_eth1)))

nc.close_session()