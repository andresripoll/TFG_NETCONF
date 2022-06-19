#!/usr/bin/python3
#0config_interface_eth1.py
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
subinterface = """
<config>
	<interfaces
		xmlns="http://openconfig.net/yang/interfaces">
		<interface>
			<name>Ethernet1</name>
			<subinterfaces>
					<subinterface>
						<index>0</index>
						<ipv4
							xmlns="http://openconfig.net/yang/interfaces/ip">
							<addresses>
								<address>
									<ip>10.1.1.1</ip>
									<config>
										<addr-type
											xmlns="http://arista.com/yang/openconfig/interfaces/augments">PRIMARY
										</addr-type>
										<ip>10.1.1.1</ip>
										<prefix-length>24</prefix-length>
									</config>
								</address>
							</addresses>
							<config>
								<enabled>true</enabled>
							</config>
							<neighbors>
								<neighbor>
									<ip>10.1.1.2</ip>
									<config>
										<ip>10.1.1.2</ip>
									</config>
								</neighbor>
							</neighbors>
						</ipv4>
					</subinterface>
				</subinterfaces>
		</interface>
	</interfaces>
</config>
"""

reply = eos.edit_config(
	target="running",
	config=subinterface,
	default_operation="merge",
)
print(reply)

eos.close_session()