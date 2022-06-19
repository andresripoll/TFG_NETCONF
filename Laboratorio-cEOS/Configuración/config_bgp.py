#!/usr/bin/python3
#config_bgp.py
#Autor: Andrés Ripoll

from ncclient import manager

eos = manager.connect(
	host = "172.20.20.3", 
	port = "830", 
	username = "admin",
	password = "admin",
	hostkey_verify = False,
	device_params = {'name':'default'},
	look_for_keys = False, 
	allow_agent = False
)

#Set Configurations
bgp = """
<config>
	<network-instances
		xmlns="http://openconfig.net/yang/network-instance">
		<network-instance>
			<name>default</name>
			<arista-varp
				xmlns="http://arista.com/yang/experimental/eos/varp/net-inst">
				<config>
					<virtual-mac-address>00:00:00:00:00:00</virtual-mac-address>
				</config>
			</arista-varp>
			<config>
				<enabled>true</enabled>
				<enabled-address-families
					xmlns:oc-types="http://openconfig.net/yang/openconfig-types">oc-types:IPV4
					
				</enabled-address-families>
				<name>default</name>
				<type
					xmlns:oc-ni-types="http://openconfig.net/yang/network-instance-types">oc-ni-types:DEFAULT_INSTANCE
					
				</type>
			</config>
			<mpls>
				<global>
					<reserved-label-blocks>
						<reserved-label-block>
							<local-id>static</local-id>
							<config>
								<local-id>static</local-id>
								<lower-bound>16</lower-bound>
								<upper-bound>99999</upper-bound>
							</config>
						</reserved-label-block>
						<reserved-label-block>
							<local-id>isis-sr</local-id>
							<config>
								<local-id>isis-sr</local-id>
								<lower-bound>900000</lower-bound>
								<upper-bound>965535</upper-bound>
							</config>
						</reserved-label-block>
						<reserved-label-block>
							<local-id>bgp-sr</local-id>
							<config>
								<local-id>bgp-sr</local-id>
								<lower-bound>900000</lower-bound>
								<upper-bound>965535</upper-bound>
							</config>
						</reserved-label-block>
						<reserved-label-block>
							<local-id>l2evpn</local-id>
							<config>
								<local-id>l2evpn</local-id>
								<lower-bound>1036288</lower-bound>
								<upper-bound>1048575</upper-bound>
							</config>
						</reserved-label-block>
						<reserved-label-block>
							<local-id>dynamic</local-id>
							<config>
								<local-id>dynamic</local-id>
								<lower-bound>100000</lower-bound>
								<upper-bound>362143</upper-bound>
							</config>
						</reserved-label-block>
						<reserved-label-block>
							<local-id>srlb</local-id>
							<config>
								<local-id>srlb</local-id>
								<lower-bound>965536</lower-bound>
								<upper-bound>1031071</upper-bound>
							</config>
						</reserved-label-block>
						<reserved-label-block>
							<local-id>l2evpnSharedEs</local-id>
							<config>
								<local-id>l2evpnSharedEs</local-id>
								<lower-bound>1031072</lower-bound>
								<upper-bound>1032095</upper-bound>
							</config>
						</reserved-label-block>
					</reserved-label-blocks>
				</global>
				<signaling-protocols>
					<rsvp-te>
						<global>
							<hellos>
								<config>
									<hello-interval>10000</hello-interval>
								</config>
							</hellos>
							<soft-preemption>
								<config>
									<enable>true</enable>
								</config>
							</soft-preemption>
						</global>
					</rsvp-te>
				</signaling-protocols>
			</mpls>
			<protocols>
				<protocol>
					<identifier
						xmlns:oc-pol-types="http://openconfig.net/yang/policy-types">oc-pol-types:DIRECTLY_CONNECTED
						
					</identifier>
					<name>DIRECTLY_CONNECTED</name>
					<config>
						<identifier
							xmlns:oc-pol-types="http://openconfig.net/yang/policy-types">oc-pol-types:DIRECTLY_CONNECTED
							
						</identifier>
						<name>DIRECTLY_CONNECTED</name>
					</config>
				</protocol>
				<protocol>
					<identifier
						xmlns:oc-pol-types="http://openconfig.net/yang/policy-types">oc-pol-types:BGP
						
					</identifier>
					<name>BGP</name>
					<bgp>
						<global>
							<afi-safis>
								<afi-safi>
									<afi-safi-name
										xmlns:oc-bgp-types="http://openconfig.net/yang/bgp-types">oc-bgp-types:IPV4_UNICAST
										
									</afi-safi-name>
									<config>
										<afi-safi-name
											xmlns:oc-bgp-types="http://openconfig.net/yang/bgp-types">oc-bgp-types:IPV4_UNICAST
											
										</afi-safi-name>
									</config>
								</afi-safi>
								<afi-safi>
									<afi-safi-name
										xmlns:oc-bgp-types="http://openconfig.net/yang/bgp-types">oc-bgp-types:IPV6_UNICAST
										
									</afi-safi-name>
									<config>
										<afi-safi-name
											xmlns:oc-bgp-types="http://openconfig.net/yang/bgp-types">oc-bgp-types:IPV6_UNICAST
											
										</afi-safi-name>
									</config>
								</afi-safi>
							</afi-safis>
							<config>
								<as>65001</as>
							</config>
						</global>
						<neighbors>
							<neighbor>
								<neighbor-address>10.1.1.2</neighbor-address>
								<afi-safis>
									<afi-safi>
										<afi-safi-name
											xmlns:oc-bgp-types="http://openconfig.net/yang/bgp-types">oc-bgp-types:IPV4_UNICAST
											
										</afi-safi-name>
										<config>
											<afi-safi-name
												xmlns:oc-bgp-types="http://openconfig.net/yang/bgp-types">oc-bgp-types:IPV4_UNICAST
												
											</afi-safi-name>
										</config>
									</afi-safi>
									<afi-safi>
										<afi-safi-name
											xmlns:oc-bgp-types="http://openconfig.net/yang/bgp-types">oc-bgp-types:IPV6_UNICAST
											
										</afi-safi-name>
										<config>
											<afi-safi-name
												xmlns:oc-bgp-types="http://openconfig.net/yang/bgp-types">oc-bgp-types:IPV6_UNICAST
												
											</afi-safi-name>
										</config>
									</afi-safi>
									<afi-safi>
										<afi-safi-name
											xmlns:oc-bgp-types="http://openconfig.net/yang/bgp-types">oc-bgp-types:L2VPN_EVPN
											
										</afi-safi-name>
										<config>
											<afi-safi-name
												xmlns:oc-bgp-types="http://openconfig.net/yang/bgp-types">oc-bgp-types:L2VPN_EVPN
												
											</afi-safi-name>
										</config>
									</afi-safi>
								</afi-safis>
								<config>
									<neighbor-address>10.1.1.2</neighbor-address>
									<peer-as>65002</peer-as>
								</config>
								<ebgp-multihop>
									<config>
										<multihop-ttl>0</multihop-ttl>
									</config>
								</ebgp-multihop>
								<transport></transport>
							</neighbor>
						</neighbors>
					</bgp>
					<config>
						<identifier
							xmlns:oc-pol-types="http://openconfig.net/yang/policy-types">oc-pol-types:BGP
							
						</identifier>
						<name>BGP</name>
					</config>
				</protocol>
			</protocols>
			<segment-routing>
				<srgbs>
					<srgb>
						<local-id>isis-sr</local-id>
						<config>
							<dataplane-type>MPLS</dataplane-type>
							<local-id>isis-sr</local-id>
							<mpls-label-blocks>isis-sr</mpls-label-blocks>
						</config>
					</srgb>
				</srgbs>
				<srlbs>
					<srlb>
						<local-id>srlb</local-id>
						<config>
							<dataplane-type>MPLS</dataplane-type>
							<local-id>srlb</local-id>
							<mpls-label-block>srlb</mpls-label-block>
						</config>
					</srlb>
				</srlbs>
			</segment-routing>
			<tables>
				<table>
					<protocol
						xmlns:oc-pol-types="http://openconfig.net/yang/policy-types">oc-pol-types:DIRECTLY_CONNECTED
						
					</protocol>
					<address-family
						xmlns:oc-types="http://openconfig.net/yang/openconfig-types">oc-types:IPV4
						
					</address-family>
					<config>
						<address-family
							xmlns:oc-types="http://openconfig.net/yang/openconfig-types">oc-types:IPV4
							
						</address-family>
						<protocol
							xmlns:oc-pol-types="http://openconfig.net/yang/policy-types">oc-pol-types:DIRECTLY_CONNECTED
							
						</protocol>
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
						<address-family
							xmlns:oc-types="http://openconfig.net/yang/openconfig-types">oc-types:IPV6
							
						</address-family>
						<protocol
							xmlns:oc-pol-types="http://openconfig.net/yang/policy-types">oc-pol-types:DIRECTLY_CONNECTED
							
						</protocol>
					</config>
				</table>
				<table>
					<protocol
						xmlns:oc-pol-types="http://openconfig.net/yang/policy-types">oc-pol-types:BGP
						
					</protocol>
					<address-family
						xmlns:oc-types="http://openconfig.net/yang/openconfig-types">oc-types:IPV4
						
					</address-family>
					<config>
						<address-family
							xmlns:oc-types="http://openconfig.net/yang/openconfig-types">oc-types:IPV4
							
						</address-family>
						<protocol
							xmlns:oc-pol-types="http://openconfig.net/yang/policy-types">oc-pol-types:BGP
							
						</protocol>
					</config>
				</table>
				<table>
					<protocol
						xmlns:oc-pol-types="http://openconfig.net/yang/policy-types">oc-pol-types:BGP
						
					</protocol>
					<address-family
						xmlns:oc-types="http://openconfig.net/yang/openconfig-types">oc-types:IPV6
						
					</address-family>
					<config>
						<address-family
							xmlns:oc-types="http://openconfig.net/yang/openconfig-types">oc-types:IPV6
							
						</address-family>
						<protocol
							xmlns:oc-pol-types="http://openconfig.net/yang/policy-types">oc-pol-types:BGP
							
						</protocol>
					</config>
				</table>
			</tables>
			<vlans>
				<vlan>
					<vlan-id>1</vlan-id>
					<config>
						<name>default</name>
						<vlan-id>1</vlan-id>
					</config>
				</vlan>
			</vlans>
		</network-instance>
	</network-instances>
</config>
"""

reply = eos.edit_config(
	target="running",
	config=bgp,
	default_operation="merge",
)
print(reply)

eos.close_session()