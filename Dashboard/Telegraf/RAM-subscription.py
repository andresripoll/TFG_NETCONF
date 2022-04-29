#!/usr/bin/env python3
#RAM-subscription.py
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
    memory_stats_array = []

    for memory_entry in rpc_reply_dict['notification']['push-update']['datastore-contents-xml']["memory-statistics"]["memory-statistic"]:
        memory_dict = {
            "name": memory_entry["name"],
            "percent_used": ( int(memory_entry["used-memory"])/int(memory_entry["total-memory"]) ) * 100,
            "field": "memory_pool"
        }  # need to use the sum by clause on PromQL to find freed bytes in CPU
        memory_stats_array.append(memory_dict)

    return json.dumps(memory_stats_array)  # return JSON formatted data

def main():
	with manager.connect(**nc) as m:
		subs = ["/memory-ios-xe-oper:memory-statistics/memory-statistic"]
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