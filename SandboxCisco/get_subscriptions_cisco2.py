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
    rcp = f"""
        <create-subscription>
            <stream>NETCONF</stream>
        </create-subscription>
    """
    response = m.dispatch(fromstring(rcp))
    python_resp = xmltodict.parse(response.xml)
    sub_data = m.take_notification()
    python_sub_data = xmltodict.parse(sub_data.notification_xml)
    print(
        f"Sub ID: {python_sub_data['notification']['push-update']['subscription-id']}")
