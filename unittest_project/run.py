# -*- coding: UTF-8 -*-
import unittest
from BeautifulReport import BeautifulReport


if __name__ == '__main__':
    # 查找unittest测试类
    test_suite = unittest.defaultTestLoader.discover('.', pattern='PO.py')
    # 调用BeautifulReport执行测试类：还是在使用unittest执行
    result = BeautifulReport(test_suite)
    result.report(filename='../lib/report/测试结果报告.html', description='测试deafult报告', log_path='.')
