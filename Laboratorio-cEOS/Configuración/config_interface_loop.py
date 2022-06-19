#!/usr/bin/python3
#config_interface_loop.py
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
loopback = """
<config>
	<interfaces
		xmlns="http://openconfig.net/yang/interfaces">
		<interface>
				<name>Loopback0</name>
				<config>
					<load-interval
						xmlns="http://arista.com/yang/openconfig/interfaces/augments">300
					</load-interval>
					<loopback-mode>true</loopback-mode>
					<name>Loopback0</name>
					<type
						xmlns:ianaift="urn:ietf:params:xml:ns:yang:iana-if-type">ianaift:softwareLoopback
					</type>
				</config>
				<subinterfaces>
					<subinterface>
						<index>0</index>
						<config></config>
						<ipv4
							xmlns="http://openconfig.net/yang/interfaces/ip">
							<addresses>
								<address>
									<ip>1.1.1.1</ip>
									<config>
										<addr-type
											xmlns="http://arista.com/yang/openconfig/interfaces/augments">PRIMARY
										</addr-type>
										<ip>1.1.1.1</ip>
										<prefix-length>32</prefix-length>
									</config>
								</address>
							</addresses>
							<config>
								<enabled>true</enabled>
							</config>
						</ipv4>
					</subinterface>
				</subinterfaces>
			</interface>
	</interfaces>
</config>
"""

reply = eos.edit_config(
	target="running",
	config=loopback,
	default_operation="merge",
)
print(reply)

eos.close_session()