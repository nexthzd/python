import unittest
import requests
from urllib import parse
from time import sleep


class weatherTest(unittest.TestCase):
    def setUp(self):
        self.url = 'http://apis.juhe.cn/simpleWeather/query?key=9ab4329466109e99d546758d0acb456f'

    def test_weather_beijing(self):
        date = {'city': '北京'}
        city = parse.urlencode(date).encode('utf-8')
        r = requests.get(self.url, params=city)
        result = r.json()

        self.assertEqual(result['reason'], '查询成功!')
        self.assertEqual(result['result']['future'][0]['date'], '2020-03-17')

    def test_weather_param_error(self):
        date = {'city': '999r'}
        r = requests.get(self.url,params=date)
        result = r.json()

        self.assertEqual(result['reason'], '暂不支持该城市')
        sleep(2)

    def test_weather_no_param(self):
        r = requests.get(self.url)
        result = r.json()

        self.assertEqual(result['reason'], '城市不能为空或暂不支持该城市')


if __name__ == '__main__':
    unittest.main()
