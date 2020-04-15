import requests
base_url='http://httpbin.org'
# r=requests.get(base_url+'/get')
# print(r.status_code)
#
# r=requests.post(base_url+'/post')
# print(r.status_code)
#
# r=requests.put(base_url+'/put')
# print(r.status_code)
#
# r=requests.delete(base_url+'/delete')
# print(r.status_code)
#
# param_date={'user':'alan','passwd':'1234'}
# r=requests.get(base_url+'/get',params=param_date)
# print(r.url)
# print(r.status_code)
#
# form_date={'user':"zl",'passwd':'123'}
# header={'user-agent':'Chrome/8.0'}
# r=requests.post(base_url+'/post',data=form_date,headers=header)
# print(r.text)
# print(r.status_code)
# print(r.he
# print(r.json())aders)

# cookie={'user':'vlan','passwd':'value'}
# r=requests.get(base_url+'/cookies',cookies=cookie)
# print(r.text)
#
# r=requests.get('http://www.baidu.com')
# print(r.cookies)
# for key,value in r.cookies.items():
#     print(key,':',value)
#
# r=requests.get(base_url+'/cookies',cookies=cookie,timeout=1000)
# print(r.text)
# file={'file':open('cat.png','rb')}
# r=requests.post(base_url+'/post',files=file)
# print(r.text)
# file={'file':open('cat.png','wb')}
# r=requests.post(base_url+'/post',files=file)
# print(r.text)
# cookie={'user':'alan','passwd':'123'}
# r=requests.get(base_url+'/cookies/set/user/51zxw')
# print(r.url)
# print(r.text)
# r=requests.get(base_url+'/cookies')
# print(r.text)
# #生成会话对象
# s= requests.session()
# r=s.get(base_url+'/cookies/set/alan/123')
# print(r.text)
# #h获取cookies值
# r=s.get(base_url+'/cookies')
# print(r.text)

# r=requests.get('https://www.12306.cn',verify=False)
# print(r.text)
#代理设置
# proxies={'http':'http://110.43.42.237:8080'}
# r=requests.get(base_url+'/get',proxies=proxies)
# print(r.text)
#身份认证
from requests.auth import HTTPBasicAuth
from requests.auth import HTTPDigestAuth
# 身份认证BasicAuth
# r=requests.get(base_url+'/basic-auth/alan/888',auth=HTTPBasicAuth('alan','888'))
# print(r.text)
# r=requests.get(base_url+'/digest-auth/auth/alan2/8887',auth=HTTPDigestAuth('alan2','8887'))
# print(r.text)
# 流式请求
import json
r=requests.get(base_url+'/stream/10',stream=True)
print(r.url)
# 如果响应内容没有设置编码，则默认设置为utf-8
# if r.encoding is None:
#     r.encoding='utf-8'
# # 对响应结果进行迭代处理
# for line in r.iter_lines(decode_unicode=True):
#     if line:
#         data=json.loads(line)
#         print(data['origin'])
from urllib import parse
date={'city':'上海'}
city=parse.urlencode(date).encode('utf-8')
url='http://apis.juhe.cn/simpleWeather/query?&key=9ab4329466109e99d546758d0acb456f'

r=requests.get(url,params=city)
# print(r.text)
# print(type(r))
respon_data=r.json()
# respon_data=json.dumps(respon_data1)
# print(type(respon_data))
print(respon_data['reason'])
print(respon_data['result'])
print(respon_data['result']['realtime']['temperature'])
print(respon_data['result']['realtime']['humidity'])
print(respon_data['result']['realtime']['info'])
print(respon_data['result']['future'][0]['date'])
print(respon_data['result']['future'][0]['wid'])
print(respon_data['result']['future'][0]['direct'])






