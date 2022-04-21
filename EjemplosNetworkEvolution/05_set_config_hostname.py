#!/usr/bin/python3

from ncclient import manager

RTR1_MGR = manager.connect(
	host = "csr3.test.lab", 
	port = "830", 
	username = "admin",
	password = "admin",
	hostkey_verify = False,
	device_params = {'name':'csr'}
)

CONFIGURATION = """
<filter>
<native
	xmlns="http://cisco.com/ns/yang/Cisco-IOS-XE-native">
	<hostname>test1234</hostname>
</native>
</filter>
"""

DATA = RTR1_MGR.get_config(CONFIGURATION, target = 'running')
print(DATA)
RTR1_MGR.close_session()