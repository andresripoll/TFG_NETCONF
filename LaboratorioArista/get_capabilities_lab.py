#!/usr/bin/env python
#Autor: Andrés Ripoll

from ncclient import manager
import sys

HOST = '172.20.20.2'
PORT = 830
USER = 'admin'
PASS = 'xxxx'

def main():
    """
    Main method that prints netconf capabilities of remote device.
    """
    with manager.connect(host=HOST, port=PORT, username=USER,
                         password=PASS, hostkey_verify=False,
                         device_params={'name': 'default'},
                         look_for_keys=False, allow_agent=False) as m:

        # print all NETCONF capabilities
        print('***Here are the Remote Devices Capabilities***')
        for capability in m.server_capabilities:
            print(capability.split('?')[0])

if __name__ == '__main__':
    sys.exit(main())
