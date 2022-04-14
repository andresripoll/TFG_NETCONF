#!/usr/bin/python3
#05_get_config_filterbyinterface_arista.py
#Autor: Andrés Ripoll

from ncclient import manager

eos = manager.connect(
	host = "172.20.20.2", 
	port = "830", 
	username = "admin",
	password = "xxxx",
	hostkey_verify = False,
	device_params = {'name':'default'},
	look_for_keys = False, 
	allow_agent = False
)

#Get Configurations
Interface_eth1 = """
<interfaces
	xmlns="http://openconfig.net/yang/interfaces">
	<interface>
		<name>Ethernet1</name>
	</interface>
</interfaces>
"""
print(eos.get_config(source="running", filter=("subtree", Interface_eth1)))
