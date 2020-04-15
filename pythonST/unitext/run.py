import unittest
from BSTestRunner import BSTestRunner
import time

test_dir = './text_case'
reports_dir ='./reports'

discover=unittest.defaultTestLoader.discover(test_dir,pattern='demo2.py')
now=time.strftime('%Y-%m-%d %H_%M_%S')
report_name=reports_dir+'/'+now+'test_report.html'

with open(report_name,'wb')as f:
    runner=BSTestRunner(stream=f,title='weater api text report',description='北京天气预报')
    runner.run(discover)

