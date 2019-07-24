import requests
import re
from bs4 import BeautifulSoup
url = "https://www.novinsamak.com/"
def recurse(url):
    code = requests.get(url)
    plain = code.text
    s = BeautifulSoup (plain, "html.parser")
    for link in s.findAll('a'):
        tet = link.get('href')
        if re.search('https://www.novinsamak.com.*', tet):
            print(tet.rstrip())
recurse(url)
