#!/usr/bin/python3
#config_interface_gb2.py
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
gb2_native = """
<config
	xmlns="urn:ietf:params:xml:ns:netconf:base:1.0">
	<native
		xmlns="http://cisco.com/ns/yang/Cisco-IOS-XE-native">
		<interface>
			<GigabitEthernet>
				<name>2</name>
				<ip>
					<address>
						<primary>
							<address>10.1.1.2</address>
							<mask>255.255.255.0</mask>
						</primary>
					</address>
				</ip>
				<logging>
					<event>
						<link-status/>
					</event>
				</logging>
				<mop>
					<enabled>false</enabled>
					<sysid>false</sysid>
				</mop>
				<negotiation
					xmlns="http://cisco.com/ns/yang/Cisco-IOS-XE-ethernet">
					<auto>true</auto>
				</negotiation>
			</GigabitEthernet>
		</interface>
	</native>
</config>
"""

reply = nc.edit_config(
	config=gb2_native,
	target="running",
)
print(reply)

gb2_interfaces = """
<config
	xmlns="urn:ietf:params:xml:ns:netconf:base:1.0">
	<interfaces
		xmlns="urn:ietf:params:xml:ns:yang:ietf-interfaces">
		<interface>
			<name>GigabitEthernet2</name>
			<type
				xmlns:ianaift="urn:ietf:params:xml:ns:yang:iana-if-type">ianaift:ethernetCsmacd
				
			</type>
			<enabled>true</enabled>
			<ipv4
				xmlns="urn:ietf:params:xml:ns:yang:ietf-ip">
				<address>
					<ip>10.1.1.2</ip>
					<netmask>255.255.255.0</netmask>
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
	config=gb2_interfaces,
	target="running",
)
print(reply)

gb2_interfaces_2 = """
<config
	xmlns="urn:ietf:params:xml:ns:netconf:base:1.0">
	<interfaces
		xmlns="http://openconfig.net/yang/interfaces">
		<interface>
			<name>GigabitEthernet2</name>
			<config>
				<name>GigabitEthernet2</name>
				<type
					xmlns:ianaift="urn:ietf:params:xml:ns:yang:iana-if-type">ianaift:ethernetCsmacd
					
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
								<ip>10.1.1.2</ip>
								<config>
									<ip>10.1.1.2</ip>
									<prefix-length>24</prefix-length>
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
			<ethernet
				xmlns="http://openconfig.net/yang/interfaces/ethernet">
				<config>
					<mac-address>52:54:00:1c:20:01</mac-address>
					<auto-negotiate>true</auto-negotiate>
					<enable-flow-control>true</enable-flow-control>
				</config>
			</ethernet>
		</interface>
	</interfaces>
</config>
"""

reply = nc.edit_config(
	config=gb2_interfaces_2,
	target="running",
)
print(reply)

nc.close_session()