#!/usr/bin/python3
#04_get_config_filterbyhostname_cisco.py
#Autor: Andrés Ripoll

from ncclient import manager

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

# #Get Configurations
# STREAM = """
# <rpc xmlns="urn:ietf:params:netconf:base:1.1" message-id="1">
#     <get>
#         <filter>
#             <manageEvent:netconf xmlns:manageEvent="urn:ietf:params:xml:ns:netmod:notification" />
#         </filter>
#     </get>
# </rpc>
# """
# print(nc.create_subscription(STREAM))

data = nc.create_subscription(stream_name='NETCONF')
print(data)

while True:
	print('Waiting for next notification')

	notification = nc.take_notification(True, 10)
	print(notification.notification_xml) 

nc.close_session()