#!/usr/bin/python3
#03_get_config_cisco.py
#Autor: Andrés Ripoll

from ncclient import manager
from xml.etree.ElementTree import tostring

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
config = nc.get_config(source="running")
print(config)

mydata = tostring(config.data, encoding="unicode")
f = open("config_cisco.xml", mode = "w")
f.write(mydata)
f.close

nc.close_session()