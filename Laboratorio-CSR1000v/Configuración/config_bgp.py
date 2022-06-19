#!/usr/bin/python3
#config_bgp.py
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
bgp = """
<config
	xmlns="urn:ietf:params:xml:ns:netconf:base:1.0">
	<network-instances
		xmlns="http://openconfig.net/yang/network-instance">
		<network-instance>
			<name>default</name>
			<config>
				<name>default</name>
				<type
					xmlns:oc-ni-types="http://openconfig.net/yang/network-instance-types">oc-ni-types:DEFAULT_INSTANCE
					
				</type>
				<description>default-vrf [read-only]</description>
			</config>
			<tables>
				<table>
					<protocol
						xmlns:oc-pol-types="http://openconfig.net/yang/policy-types">oc-pol-types:DIRECTLY_CONNECTED
						
					</protocol>
					<address-family
						xmlns:oc-types="http://openconfig.net/yang/openconfig-types">oc-types:IPV4
						
					</address-family>
					<config>
						<protocol
							xmlns:oc-pol-types="http://openconfig.net/yang/policy-types">oc-pol-types:DIRECTLY_CONNECTED
							
						</protocol>
						<address-family
							xmlns:oc-types="http://openconfig.net/yang/openconfig-types">oc-types:IPV4
							
						</address-family>
					</config>
				</table>
				<table>
					<protocol
						xmlns:oc-pol-types="http://openconfig.net/yang/policy-types">oc-pol-types:DIRECTLY_CONNECTED
						
					</protocol>
					<address-family
						xmlns:oc-types="http://openconfig.net/yang/openconfig-types">oc-types:IPV6
						
					</address-family>
					<config>
						<protocol
							xmlns:oc-pol-types="http://openconfig.net/yang/policy-types">oc-pol-types:DIRECTLY_CONNECTED
							
						</protocol>
						<address-family
							xmlns:oc-types="http://openconfig.net/yang/openconfig-types">oc-types:IPV6
							
						</address-family>
					</config>
				</table>
				<table>
					<protocol
						xmlns:oc-pol-types="http://openconfig.net/yang/policy-types">oc-pol-types:STATIC
						
					</protocol>
					<address-family
						xmlns:oc-types="http://openconfig.net/yang/openconfig-types">oc-types:IPV4
						
					</address-family>
					<config>
						<protocol
							xmlns:oc-pol-types="http://openconfig.net/yang/policy-types">oc-pol-types:STATIC
							
						</protocol>
						<address-family
							xmlns:oc-types="http://openconfig.net/yang/openconfig-types">oc-types:IPV4
							
						</address-family>
					</config>
				</table>
				<table>
					<protocol
						xmlns:oc-pol-types="http://openconfig.net/yang/policy-types">oc-pol-types:STATIC
						
					</protocol>
					<address-family
						xmlns:oc-types="http://openconfig.net/yang/openconfig-types">oc-types:IPV6
						
					</address-family>
					<config>
						<protocol
							xmlns:oc-pol-types="http://openconfig.net/yang/policy-types">oc-pol-types:STATIC
							
						</protocol>
						<address-family
							xmlns:oc-types="http://openconfig.net/yang/openconfig-types">oc-types:IPV6
							
						</address-family>
					</config>
				</table>
			</tables>
			<protocols>
				<protocol>
					<identifier
						xmlns:oc-pol-types="http://openconfig.net/yang/policy-types">oc-pol-types:BGP
						
					</identifier>
					<name>65002</name>
					<config>
						<identifier
							xmlns:oc-pol-types="http://openconfig.net/yang/policy-types">oc-pol-types:BGP
							
						</identifier>
						<name>65002</name>
					</config>
					<bgp>
						<global>
							<config>
								<as>65002</as>
							</config>
							<graceful-restart>
								<config>
									<enabled>false</enabled>
								</config>
							</graceful-restart>
							<route-selection-options>
								<config>
									<always-compare-med>false</always-compare-med>
									<external-compare-router-id>true</external-compare-router-id>
								</config>
							</route-selection-options>
						</global>
						<neighbors>
							<neighbor>
								<neighbor-address>10.1.1.1</neighbor-address>
								<config>
									<neighbor-address>10.1.1.1</neighbor-address>
									<peer-as>65001</peer-as>
								</config>
								<timers>
									<config>
										<hold-time>180.0</hold-time>
										<keepalive-interval>60.0</keepalive-interval>
									</config>
								</timers>
								<ebgp-multihop>
									<config>
										<enabled>false</enabled>
									</config>
								</ebgp-multihop>
							</neighbor>
						</neighbors>
					</bgp>
				</protocol>
				<protocol>
					<identifier
						xmlns:oc-pol-types="http://openconfig.net/yang/policy-types">oc-pol-types:STATIC
						
					</identifier>
					<name>DEFAULT</name>
					<config>
						<identifier
							xmlns:oc-pol-types="http://openconfig.net/yang/policy-types">oc-pol-types:STATIC
							
						</identifier>
						<name>DEFAULT</name>
					</config>
				</protocol>
				<protocol>
					<identifier
						xmlns:oc-pol-types="http://openconfig.net/yang/policy-types">oc-pol-types:DIRECTLY_CONNECTED
						
					</identifier>
					<name>DEFAULT</name>
					<config>
						<identifier
							xmlns:oc-pol-types="http://openconfig.net/yang/policy-types">oc-pol-types:DIRECTLY_CONNECTED
							
						</identifier>
						<name>DEFAULT</name>
					</config>
				</protocol>
			</protocols>
		</network-instance>
	</network-instances>
</config>
"""

reply = nc.edit_config(
	config=bgp,
	target="running",
)
print(reply)

nc.close_session()