# collecting json data through API

import requests

url = 'http://www.omdbapi.com/?apikey=6fb4480b&t=the+social+network'
r = requests.get(url)

# reading raw
print(r.text+ '\n')

# read it in json format though
json_data = r.json()
for k in json_data.keys():
    print(k + ': ', json_data[k])
