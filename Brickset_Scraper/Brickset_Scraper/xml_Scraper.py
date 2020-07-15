from lxml import etree
import json

result = []
result1 = []

root = etree.parse('page.xml').getroot()

for item in root.findall('item'):
    name = item.find('name').text
    pieces = item.find('pieces').text
    minifigs = item.find('minifigs').text
    image = item.find('image').text
    community = item.find('community').text
    needs = item.find('needs').text
    buy_at = item.find('buy_at').text
    buy_at2 = item.find('buy_at2').text
    buy_at3 = item.find('buy_at3').text
    buy_at4 = item.find('buy_at4').text
    result.append(("name:"+name, "pieces :"+pieces, "minifigs :"+minifigs, "image:"+image, "community :"+community, "needs :"+needs, "buy_at :"+buy_at, buy_at2, buy_at3, buy_at4))

for i in range(len(result)):
    for x in result:
        result1.append(x)
with open('page12.json', 'w') as f:
    json.dump(result1, f)

# for item in root[0]:
#     print(item.tag, item.attrib)
#
# for item in root[0]:
#     print(item.text)


