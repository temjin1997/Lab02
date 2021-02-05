from ncclient import manager
import xml.dom.minidom

"""
router = {"host": "ios-xe-mgmt-latest.cisco.com", "port": "10000",
          "username": "developer", "password": "C1sco12345"}

router = {"host": "10.50.50.19", "port": "22",
          "username": "admin", "password": "P@ssw0rd123"}

"""
router = {"host": "10.50.50.20", "port": "830",
          "username": "cisco", "password": "cisco"}

netconf_filter = """
 <filter>
  <interfaces xmlns="urn:ietf:params:xml:ns:yang:ietf-interfaces">
    <interface>
      <name>GigabitEthernet1</name>
    </interface>
  </interfaces>
  <interfaces-state xmlns="urn:ietf:params:xml:ns:yang:ietf-interfaces">
    <interface>
      <name>GigabitEthernet1</name>
    </interface>
  </interfaces-state>
</filter>
"""

with manager.connect(host=router["host"], port=router["port"], username=router["username"], password=router["password"], hostkey_verify=False) as m:
    for capability in m.server_capabilities:
        print('*' * 50)
        print(capability)

        interface_netconf = m.get(netconf_filter)
        xmlDom = xml.dom.minidom.parseString(str(interface_netconf))
        print (xmlDom.toprettyxml(indent="  "))
        print ('*'*25 + 'Break' + '*'*50)




#   m.close_session()