#!/usr/bin/python3
#01_get_capabilities_cisco.py
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

#Get Capabilities
for capability in nc.server_capabilities:
	print(capability.split('?')[0])

nc.close_session()