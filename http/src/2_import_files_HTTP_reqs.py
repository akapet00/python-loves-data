from urllib.request import urlopen, Request
import requests

url = "http://www.datacamp.com/teach/documentation"

req = Request(url)
print('req type is {}'.format(type(req)))

res = urlopen(req)
print('res type is {}'.format(type(res)))

# read what you get
html = res.read()
print(html)

# closing the response
res.close()


# easier way is using the request library
r = requests.get(url)
data = r.text # returns pretty, indented HTML data record
print(data)
# no need to close the response when using requests
