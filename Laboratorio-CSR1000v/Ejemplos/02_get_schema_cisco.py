#!/usr/bin/python3
#02_get_schema_cisco.py
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

#Get Schema
SCHEMA = nc.get_schema("cisco-xe-ietf-event-notifications-deviation")
print(SCHEMA)

nc.close_session()