import os
import json
import glob

path = 'C:\\Users\\aravi\\PycharmProjects\\Brickset-Scraper\\Brickset_Scraper\\Brickset_Scraper\\Data-Full\\*.json\\'

files = glob.glob(path)

empty = []

for file in files:
    f = open(file,'r')
    funny = '%s' %f.readline()
    empty.append(funny)


#for r, d, f in os.walk(path):
    # r = root, d = directories, f = files
#    for file in f:
#       if '.json' in file:
#            files.append(os.path.join(r, file))

# entries = os.listdir('C:\\Users\\aravi\\PycharmProjects\\Brickset-Scraper\\Brickset_Scraper\\Brickset_Scraper\\Data-Full\\')

j = []

for i in empty:
    q = ({'name': i['name'], 'minifigs': i['minifigs']})
    j.append(q)

with open('folder.json', 'w') as jsonD:
    json.dump(j, jsonD)
    jsonD.close()
