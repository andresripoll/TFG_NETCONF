from ncclient import manager
# https://community.cisco.com/t5/devnet-sandbox/
# connect-to-ios-xr-always-on-sandbox-using-ncclient/td-p/4442858
nc=manager.connect(
            host = "sandbox-iosxr-1.cisco.com", 
			port = "22", 
			timeout = 30,
            username = "admin",
            password = "C1sco12345",
            hostkey_verify=False,
            look_for_keys=False,
            allow_agent=False)
			
capabilities = nc.server_capabilities

for capability in nc.server_capabilities:
            print(capability.split('?')[0])