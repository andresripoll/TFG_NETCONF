from ncclient import manager

eos = manager.connect(
    host="172.20.20.2",
    port="830",
    timeout=30,
    username="admin",
    password="xxxx",
    hostkey_verify=False,
)

#Get Configurations
print(eos.get_config())

eos.close_session()
