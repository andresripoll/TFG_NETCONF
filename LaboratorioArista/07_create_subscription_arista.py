#!/usr/bin/python3
#06_create_subscription_arista.py
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


# #Create subscription
# cfg_hostname = """
# <rpc xmlns="urn:ietf:params:xml:ns:netconf:base:1.0" message-id="1">
#     <create-subscription xmlns="urn:ietf:params:xml:ns:netconf:notification:1.0">
#         <stream>NETCONF</stream>
#     </create-subscription>
# </rpc>
# """

# reply = eos.edit_config(
# 	target="running",
# 	config=cfg_hostname,
# 	default_operation="merge",
# )
# print(reply)

data = eos.create_subscription(stream_name='NETCONF')
print(data)

while True:
	print('Waiting for next notification')

	notification = eos.take_notification(True, 10)
	print(notification.notification_xml) 

eos.close_session()
