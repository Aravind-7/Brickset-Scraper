import os
import json
import pprint
import ast

path = "C:\\Users\\aravi\\PycharmProjects\\Brickset-Scraper\\Brickset_Scraper\\Brickset_Scraper\\Data-Full\\"

values = []

for file in os.listdir(path):
   f = open(path+file, 'r', encoding='utf-8')
   values.append(f.readlines())

print(len(values))

listname = []

for i in range(len(values)):
    for j in range(1,len(values[i])):
        try :
            if values[i][j] == '[\n' or values[i][j] == ']':
                print(values[i][j])
            else:
                l = ast.literal_eval(values[i][j])
                l = json.load(val)
                q = ({'name': l['name'], 'minifigs': l['minifigs']})
                listname.append(q)
        except Exception as e:
            print(e)
pprint.pprint(listname)







