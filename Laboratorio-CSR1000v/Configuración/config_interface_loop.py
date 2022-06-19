#!/usr/bin/python3
#config_interface_loop.py
#Autor: Andrés Ripoll

from ncclient import manager
from lxml import etree

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

#Set Configurations
loop_native = """
<config
	xmlns="urn:ietf:params:xml:ns:netconf:base:1.0">
	<native
		xmlns="http://cisco.com/ns/yang/Cisco-IOS-XE-native">
		<interface>
			<Loopback>
				<name>0</name>
				<ip>
					<address>
						<primary>
							<address>2.2.2.2</address>
							<mask>255.255.255.255</mask>
						</primary>
					</address>
				</ip>
				<logging>
					<event>
						<link-status/>
					</event>
				</logging>
			</Loopback>
		</interface>
	</native>
</config>
"""

reply = nc.edit_config(
	config=loop_native,
	target="running",
)
print(reply)

loop_interfaces = """
<config
	xmlns="urn:ietf:params:xml:ns:netconf:base:1.0">
	<interfaces
		xmlns="urn:ietf:params:xml:ns:yang:ietf-interfaces">
		<interface>
			<name>Loopback0</name>
			<type
				xmlns:ianaift="urn:ietf:params:xml:ns:yang:iana-if-type">ianaift:softwareLoopback
				
			</type>
			<enabled>true</enabled>
			<ipv4
				xmlns="urn:ietf:params:xml:ns:yang:ietf-ip">
				<address>
					<ip>2.2.2.2</ip>
					<netmask>255.255.255.255</netmask>
				</address>
			</ipv4>
			<ipv6
				xmlns="urn:ietf:params:xml:ns:yang:ietf-ip">
			</ipv6>
		</interface>
	</interfaces>
</config>
"""

reply = nc.edit_config(
	config=loop_interfaces,
	target="running",
)
print(reply)

loop_interfaces_2 = """
<config
	xmlns="urn:ietf:params:xml:ns:netconf:base:1.0">
	<interfaces
		xmlns="http://openconfig.net/yang/interfaces">
		<interface>
			<name>Loopback0</name>
			<config>
				<name>Loopback0</name>
				<type
					xmlns:ianaift="urn:ietf:params:xml:ns:yang:iana-if-type">ianaift:softwareLoopback
					
				</type>
				<enabled>true</enabled>
			</config>
			<subinterfaces>
				<subinterface>
					<index>0</index>
					<config>
						<index>0</index>
						<enabled>true</enabled>
					</config>
					<ipv4
						xmlns="http://openconfig.net/yang/interfaces/ip">
						<addresses>
							<address>
								<ip>2.2.2.2</ip>
								<config>
									<ip>2.2.2.2</ip>
									<prefix-length>32</prefix-length>
								</config>
							</address>
						</addresses>
					</ipv4>
					<ipv6
						xmlns="http://openconfig.net/yang/interfaces/ip">
						<config>
							<enabled>false</enabled>
						</config>
					</ipv6>
				</subinterface>
			</subinterfaces>
		</interface>
	</interfaces>
</config>
"""

reply = nc.edit_config(
	config=loop_interfaces_2,
	target="running",
)
print(reply)

nc.close_session()