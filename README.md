# web-crawler
# A web crawler in python 
import requests
from bs4 import BeautifulSoup
url = "Your_Desired_Url"
code = requests.get(url)
plain = code.text
s = BeautifulSoup (plain, "html.parser")
for link in s.findAll('a'):
        tet = link.get('href')
        print(tet)
# This small python script starts to crawwl a giving URL and prints all links in the page.
