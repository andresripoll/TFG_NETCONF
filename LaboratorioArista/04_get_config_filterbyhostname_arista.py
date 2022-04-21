#!/usr/bin/python3
#04_get_config_filterbyhostname_arista.py
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
hostname = """
<system
	xmlns="http://openconfig.net/yang/system">
	<config>
		<hostname>
		</hostname>
	</config>
</system>
"""
print(eos.get_config(source="running", filter=("subtree", hostname)))

eos.close_session()
