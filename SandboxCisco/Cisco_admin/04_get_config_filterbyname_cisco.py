#!/usr/bin/python3
#04_get_config_filterbyname_cisco.py
#Autor: Andrés Ripoll

from ncclient import manager

nc = manager.connect(
	host = "sandbox-iosxr-1.cisco.com", 
	port = "22", 
	timeout = 30,
	username = "admin",
	password = "C1sco12345",
	hostkey_verify = False,
	look_for_keys = False,
	allow_agent = False
)

#Get Configurations
FILTER = """
<filter>
	<aaa xmlns="http://cisco.com/ns/yang/Cisco-IOS-XR-aaa-lib-cfg">
		<usernames xmlns="http://cisco.com/ns/yang/Cisco-IOS-XR-aaa-locald-cfg">
			<username>
				<ordering-index>1</ordering-index>
     			<name></name>
			</username>
		</usernames>
	</aaa>
</filter>
"""
print(nc.get_config('running', FILTER))

nc.close_session()