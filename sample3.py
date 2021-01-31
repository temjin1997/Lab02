import xmltodict

stream = open('sample.xml','r')

xml = xmltodict.parse(stream.read())

print(type(xml['People']))

print(type(xml['People']['Person']))

for e in xml['People']['Person']:
    print(e)

