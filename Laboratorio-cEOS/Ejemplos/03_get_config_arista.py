#!/usr/bin/python3
#03_get_config_arista.py
#Autor: Andrés Ripoll

from ncclient import manager

eos = manager.connect(
	host = "172.20.20.2", 
	port = "830", 
	username = "admin",
	password = "xxxx",
	hostkey_verify = False,
	device_params = {'name':'default'},
	look_for_keys = False, 
	allow_agent = False
)

#Get Configurations
config = eos.get_config(source="running")
print(config)

mydata = open("config_arista.xml", mode = "w")
mydata.write(str(config))
mydata.close

eos.close_session()
