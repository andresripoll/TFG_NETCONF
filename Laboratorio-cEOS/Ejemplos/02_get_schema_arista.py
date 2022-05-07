#!/usr/bin/python3
#02_get_schema_arista.py
#Autor: Andrés Ripoll
import re
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

#Get Capabilities
capabilities = []

for capability in eos.server_capabilities:
	capabilities.append(capability)

capabilities = sorted(capabilities)

#Get Modules
modules = []

for capability in capabilities:
	supported_model = re.search('module=(.*)&', capability)
	if supported_model is not None:
		print("Supported Model: %s" % supported_model.group(1))
		modules.append(supported_model.groups(0)[0])

#Get Schema
schema = eos.get_schema('ietf-interfaces')
print(schema)

# #Get Schema
# models_desired = ['openconfig-extensions', 'openconfig-interfaces']

# for model in models_desired:
# 	schema = eos.get_schema(model)
# 	with open("./{}.yang".format(model), 'w') as f:
# 		f.write(schema.data)

eos.close_session()
