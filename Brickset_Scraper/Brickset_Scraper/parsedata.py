import json

with open('Data-Full/1983.json') as json_data:
    jsonData = json.load(json_data)

j = []

for i in jsonData:
    q = ({'name': i['name'], 'minifigs': i['minifigs']})
    j.append(q)

with open('test.json', 'w') as jsonD:
    json.dump(j, jsonD)
    jsonD.close()

