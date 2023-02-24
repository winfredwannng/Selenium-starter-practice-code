import os
import unittest

from ddt import ddt, data, unpack, file_data
import pytest


def get_data():
    testdata = [{'name': 'tom', 'age': 20}, {'name': 'kite', 'age': 22}]
    return testdata


@ddt
class MytestCase(unittest.TestCase):
    @data(1, 2, 3)
    def test1(self, value):
        print(value)

    @data((1, 2, 3), (4, 5, 6))
    def test2(self, value):
        print(value)

    @data((1, 2, 3), (4, 5, 6))
    @unpack
    def test3(self, v1, v2, v3):
        print(v1, v2, v3)

    @data(get_data())
    def test4(self, value):
        print(value)

    @file_data(os.getcwd() + '/test.json')
    def test5(self, value2):
        print(value2)


if __name__ == '__main__':
    unittest.main()
