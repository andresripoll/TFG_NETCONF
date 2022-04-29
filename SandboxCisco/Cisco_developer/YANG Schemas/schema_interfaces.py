#!/usr/bin/python3
#schema_interfaces.py
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

#Get Schema
SCHEMA = nc.get_schema("ietf-interfaces")
print(SCHEMA)

nc.close_session()