import json

with open('movie.json') as json_file:
    json_data = json.load(json_file)

for k  in json_data.keys():
    print(k + ': ', json_data[k])
