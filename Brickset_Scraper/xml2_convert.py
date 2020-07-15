import xmltodict
import json

with open('page.xml') as xml_file:
    my_dict = xmltodict.parse(xml_file.read())
    xml_file.close()

with open('my.json','w') as json_file:
    json.dump(my_dict,json_file)