import os, json
import pandas as pd
import sys

path_to_json = 'C:\\Users\\aravi\\PycharmProjects\\Brickset-Scraper\\Brickset_Scraper\\Brickset_Scraper\\Data-Full\\'
json_files =[pos_json for pos_json in os.listdir(path_to_json) if pos_json.endswith('.json')]

word_1 = sys.argv[1]
word_2 = sys.argv[2]

json_data = pd.DataFrame(columns=['name', 'pieces'])

output_Data = []

for index, js in enumerate(json_files):
    with open(os.path.join(path_to_json, js)) as json_file:
        #print(index)
        json_text = json.load(json_file)
        for rec in json_text:
            #print(type(rec))
            name = ({word_1: rec[word_1], word_2: rec[word_2]})
            output_Data.append(name)
        #pieces = json_text['pieces']

        #json_data.loc[index] = [name]


print(output_Data)