#!/usr/bin/python3
#schema_memory-cpu.py
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
SCHEMA = nc.get_schema("Cisco-IOS-XE-process-memory-oper")
print(SCHEMA)

mydata = open("schema_memory_cpu.xml", mode = "w")
mydata.write(str(SCHEMA))
mydata.close

nc.close_session()