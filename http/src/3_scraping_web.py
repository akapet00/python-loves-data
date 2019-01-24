# HTML is a max of unstructured and structured data
# to create useful data from raw HTML, parsing and extracting structured data needs to be done
# BEAUTIFUL SOUP - converts 'tag soup' to parsed, pretty data

import requests
from bs4 import BeautifulSoup

url = 'https://www.python.org/~guido/'
r = requests.get(url)
html_data = r.text

# creating a BeautifulSoup object from the html
soup = BeautifulSoup(html_data, features='lxml')
print('soup datatype is: {}'.format(type(soup)))

# prettifying the BeautifulSoup object
pretty_soup = soup.prettify()
print('pretty_soup datatype is: {}'.format(type(pretty_soup)))
print('\n\ndata:\n\n{}'.format(pretty_soup))


# features
# title
title = soup.title
print(title)

# text in html
text = soup.get_text()
print(text)

# tags
a_tags = soup.find_all('a')

# links
for link in a_tags:
    print(link.get('href'))
