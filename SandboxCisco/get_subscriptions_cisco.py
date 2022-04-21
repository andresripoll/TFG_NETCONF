#!/usr/bin/env python
#Autor: Andrés Ripoll

from ncclient import manager
import logging
import xmltodict
from lxml.etree import fromstring

router = {
    "host": "sandbox-iosxr-1.cisco.com",
    "port": "22",
    "username": "admin",
    "password": "C1sco12345",
    "hostkey_verify": False,
    "look_for_keys": False,
    "allow_agent": False
}

with manager.connect(**router) as m:
    subs = ["/memory-ios-xe-oper:memory-statistics/memory-statistic"]
    for sub in subs:
        rcp = f"""
            <create-subscription xmlns='urn:ietf:params:netconf:capability:notification:1.0' xmlns:yp='urn:ietf:params:xml:ns:yang:ietf-yang-types'>
                <stream>yp:yang-types</stream>
                <yp:xpath-filter>{sub}</yp:xpath-filter>
                <yp:period>500</yp:period>
            </create-subscription>
        """
        response = m.dispatch(fromstring(rcp))
        python_resp = xmltodict.parse(response.xml)

        while True:
            sub_data = m.take_notification()
            python_sub_data = xmltodict.parse(sub_data.notification_xml)
            print(
                f"Sub ID: {python_sub_data['notification']['push-update']['subscription-id']}")
            print(
                f"Name: {python_sub_data['notification']['push-update']['datastore-contents-xml']['memory-statistics']['memory-statistic'][0]['name']}")
            print(
                f"Total RAM: {python_sub_data['notification']['push-update']['datastore-contents-xml']['memory-statistics']['memory-statistic'][0]['total-memory']}")
            print(
                f"Used RAM: {python_sub_data['notification']['push-update']['datastore-contents-xml']['memory-statistics']['memory-statistic'][0]['used-memory']}")
            print(
                f"Free RAM: {python_sub_data['notification']['push-update']['datastore-contents-xml']['memory-statistics']['memory-statistic'][0]['free-memory']}")
        
