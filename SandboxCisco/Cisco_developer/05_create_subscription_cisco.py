#!/usr/bin/python3
#04_get_config_filterbyhostname_cisco.py
#Autor: Andrés Ripoll

from ncclient import manager, operations
from ncclient.xml_ import to_ele
import logging
import xmltodict
from lxml.etree import fromstring

nc = {
	"host": "sandbox-iosxe-latest-1.cisco.com", 
	"port": "830", 
	"timeout": 30,
	"username": "developer",
	"password": "C1sco12345",
	"hostkey_verify": False,
	"look_for_keys": False,
	"allow_agent": False
}

with manager.connect(**nc) as s:
    print("Session id is: ", s.session_id)
    
    
    rpc = """
        
		
            <establish-subscription xmlns="urn:ietf:params:xml:ns:yang:ietf-event-notifications"
xmlns:yp="urn:ietf:params:xml:ns:yang:ietf-yang-push">
                <stream>yp:yang-push</stream>
                <yp:xpath-filter>/native/hostname</yp:xpath-filter>
                <yp:period>1000</yp:period>
            </establish-subscription>
        """
    request=s.dispatch(to_ele(rpc))
        

    while True:
        print("Receiving notifications...")
        sub_data=s.take_notification(timeout=30)
        if (sub_data != None):
            print(sub_data.notification_xml)
        print("------------------------")