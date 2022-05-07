#!/usr/bin/env python3
#CPU-subscription.py
#Autor: Andrés Ripoll

from ncclient import manager
from typing import Dict

import xmltodict
from lxml.etree import fromstring
import json

nc = {
	"host": "172.21.0.3", 
	"port": "830", 
	"username":"admin",
	"password": "admin",
	"hostkey_verify": False,
	"look_for_keys": False,
	"allow_agent": False
}

def dict_to_telegraf_json(rpc_reply_dict: Dict) -> str:
    cpu_process_stats_array = []

    for process_entry in rpc_reply_dict['notification']['push-update']['datastore-contents-xml']["memory-usage-processes"]["memory-usage-process"]:
        if int(process_entry["allocated-memory"]) > 0:
            process_dict = {
                "name": process_entry["name"].replace(" ", "_"),
                "process_id": int(process_entry["pid"]),
                "consumed_bytes": int(process_entry["holding-memory"]),
                "field": "cpu_process"
            }  # trying to get rate of consumption of processes
            cpu_process_stats_array.append(process_dict)

    return json.dumps(cpu_process_stats_array)  # return JSON formatted data

def main():
	with manager.connect(**nc) as m:
		subs = ["/process-memory-ios-xe-oper:memory-usage-processes/memory-usage-process"]
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