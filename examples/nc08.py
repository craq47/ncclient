#!/usr/bin/python
#
# Create a new vlan using edit_config
#
# $ ./nc08.py broccoli

import sys, os, warnings
warnings.simplefilter("ignore", DeprecationWarning)
from ncclient import manager

def demo(host, user):
    snippet = """<nc:config xmlns:nc="urn:ietf:params:xml:ns:netconf:base:1.0">
<brcd:netiron-config xmlns:brcd="http://brocade.com/ns/netconf/config/netiron-config/">
<brcd:vlan-config>
<brcd:vlan nc:operation="delete">
<brcd:vlan-id>200</brcd:vlan-id>
</brcd:vlan>
</brcd:vlan-config>
</brcd:netiron-config>
</nc:config>"""

    with manager.connect(host=host, port=830, username=user, password="pass") as m:
        m.edit_config(target='running', config=snippet)

if __name__ == '__main__':
	demo(sys.argv[1], "testuser")