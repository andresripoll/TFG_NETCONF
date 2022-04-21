#!/usr/bin/python3
#06_set_config_hostname_arista.py
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
cfg_hostname = """
<config>
	<system
		xmlns="http://openconfig.net/yang/system">
		<config>
			<hostname>test1234</hostname>
		</config>
	</system>
</config>
"""

reply = eos.edit_config(
	target="running",
	config=cfg_hostname,
	default_operation="merge",
)
print(reply)

eos.close_session()
