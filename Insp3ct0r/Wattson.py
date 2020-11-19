import requests
from bs4 import BeautifulSoup as bs
from bs4 import Comment
from re import compile

patt = compile('flag: ([\w{}_?]* ')

s = requests.session()

url = 'https://jupiter.challenges.picoctf.org/problem/44924/'

flag = ""

r = s.get(url)

soup = bs(r.text,features="html.parser")

m = patt.findall(r.text)

if m:
    flag += m[0]

htmls = ""

for link in soup.findAll('link'):
    r = s.get(url + link['href'])
    htmls += r.text
[line for line in htmls.split('\n') if 'flag' in line]

js = ""

for script in soup.findAll('script'):
    r = s.get(url + script['src'])
    js += r.text
[line for line in js.split('\n') if 'flag' in line]
