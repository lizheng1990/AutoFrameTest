# coding:utf8

import unittest

class MyTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        print("最开始运行一次\n")

    @classmethod
    def tearDownClass(cls) -> None:
        print("最后运行一次")

    def setUp(self):
        print("开始")

    def test_1(self):
        print("test_1")

    def test_2(self):
        print("test_2")

    def tearDown(self):
        print("结束")