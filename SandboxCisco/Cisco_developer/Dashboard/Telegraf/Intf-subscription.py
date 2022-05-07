#!/usr/bin/env python3
#Intf-subscription.py
#Autor: Andrés Ripoll

from ncclient import manager
from typing import Dict

import xmltodict
from lxml.etree import fromstring
import json

nc = {
	"host": "sandbox-iosxe-latest-1.cisco.com", 
	"port": "830", 
	"username":"developer",
	"password": "C1sco12345",
	"hostkey_verify": False,
	"look_for_keys": False,
	"allow_agent": False
}

def dict_to_telegraf_json(rpc_reply_dict: Dict) -> str:
    intf_stats_array = []
    for intf_entry in rpc_reply_dict['notification']['push-update']['datastore-contents-xml']["interfaces-state"]["interface"]:
        intf_stats = {}
        intf_name = intf_entry["name"].replace(" ", "_")
        intf_stats = {
            "operational_status": 1 if intf_entry["oper-status"]=="up" else 0,
            "in_octets": int(intf_entry["statistics"]["in-octets"]),
            "in_errors": int(intf_entry["statistics"]["in-errors"]),
            "out_octets": int(intf_entry["statistics"]["out-octets"]),
            "out_errors": int(intf_entry["statistics"]["out-errors"]),
            "name": intf_name,
            "field": "intf_stats"
        }
        intf_stats_array.append(intf_stats)

    return json.dumps(intf_stats_array)  # return JSON formatted data

def main():
	with manager.connect(**nc) as m:
		subs = ["/interfaces-state/interface"]
		for sub in subs:
			rcp = f"""
				<establish-subscription xmlns="urn:ietf:params:xml:ns:yang:ietf-event-notifications" xmlns:yp="urn:ietf:params:xml:ns:yang:ietf-yang-push">
					<stream>yp:yang-push</stream>
					<yp:xpath-filter>{sub}</yp:xpath-filter>
					<yp:period>500</yp:period>
				</establish-subscription>
			"""

			m.dispatch(fromstring(rcp))
			sub_data = m.take_notification()
			python_sub_data = xmltodict.parse(sub_data.notification_xml)
			telegraf_json_input = dict_to_telegraf_json(python_sub_data)
			print(telegraf_json_input)

if __name__ == "__main__":
	main()