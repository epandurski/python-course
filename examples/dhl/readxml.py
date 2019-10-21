import pdb
import xml.etree.ElementTree as ET
import requests
import sys

r = requests.get('http://localhost:8000/demo.xml')
r.raise_for_status()
xml_body = r.text
root = ET.fromstring(xml_body)
singapore_year = root.find("country[@name='Singapore']/year")

print(singapore_year.text)
singapore_year.text = '1111'
print(ET.tostring(root))

# for child in root:
#     if child.tag == 'country' and child.attrib['name'] == 'Singapore':
#         singapore = child
#         break
# else:
#     print('Can not find Singapre.')
#     sys.exit(2)
# print(singapore)
# print(singapore.attrib['name'])
# print(singapore.find('year').text)

