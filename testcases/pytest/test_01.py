import pytest


class TestLoginCase:

    def test01(self):
        print('test01')

    def test02(self):
        print('test02')


if __name__ == '__main__':
    pytest.main(['-vs', 'test_01.py'])
