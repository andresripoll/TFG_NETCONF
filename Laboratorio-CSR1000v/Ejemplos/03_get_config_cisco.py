#!/usr/bin/python3
#03_get_config_cisco.py
#Autor: Andrés Ripoll

from ncclient import manager

nc = manager.connect(
	host = "172.20.20.3", 
	port = "830", 
	timeout = 30,
	username = "admin",
	password = "admin",
	hostkey_verify = False,
	look_for_keys = False,
	allow_agent = False
)

#Get Configurations
config = nc.get_config(source="running")
print(config)

mydata = open("config_cisco.xml", mode = "w")
mydata.write(str(config))
mydata.close

nc.close_session()