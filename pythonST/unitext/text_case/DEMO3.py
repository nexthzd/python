import unittest
import requests
from urllib import parse

url='http://apis.juhe.cn/simpleWeather/query?key=9ab4329466109e99d546758d0acb456f'
param={'city':'北京'}
city=parse.urlencode(param).encode('utf-8')
r=requests.get(url=url,params=city)
print(r.text)