#!/usr/bin/python3

from ncclient import manager

RTR1_MGR = manager.connect(
	host = "csr3.test.lab", 
	port = "830", 
	username = "admin",
	password = "admin",
	hostkey_verify = False,
	device_params = {'name':'csr'})

for capability in RTR1_MGR.server_capabilities:
	print(capability)

RTR1_MGR.close_session()