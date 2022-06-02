#!/usr/bin/python3
#02_get_schema_cisco.py
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

#Get Schema
SCHEMA = nc.get_schema("Cisco-IOS-XR-ipv4-ma-subscriber-cfg")
print(SCHEMA)

mydata = open("schema_cisco.xml", mode = "w")
mydata.write(str(SCHEMA))
mydata.close

nc.close_session()