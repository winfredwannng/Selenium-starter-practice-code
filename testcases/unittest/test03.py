import unittest
import os


class MyTestCase03(unittest.TestCase):
    def test03(self):
        print('test03')

    def test04(self):
        print('test04')


if __name__ == '__main__':
    loader = unittest.TestLoader()
    suite = unittest.TestSuite()

    path = os.path.dirname(os.path.abspath(__file__))
    suite.addTest(loader.discover(path))
