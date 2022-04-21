#!/usr/bin/python3
#06_create_subscription_cisco.py
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


# #Create subscription
# cfg_hostname = """
# <rpc xmlns="urn:ietf:params:xml:ns:netconf:base:1.0" message-id="1">
#     <create-subscription xmlns="urn:ietf:params:xml:ns:netconf:notification:1.0">
#         <stream>NETCONF</stream>
#     </create-subscription>
# </rpc>
# """

# reply = nc.edit_config(
# 	target="running",
# 	config=cfg_hostname,
# 	default_operation="merge",
# )
# print(reply)

data = nc.create_subscription(stream_name='NETCONF')
print(data)

while True:
	print('Waiting for next notification')

	notification = nc.take_notification(True, 10)
	print(notification.notification_xml) 

nc.close_session()
