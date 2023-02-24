import unittest


class MyTestCase(unittest.TestCase):
    def setUp(self) -> None:
        print('setup')

    def test01(self):
        print('test01')
        self.assertEqual(1, 1)

    def test02(self):
        print('test02')
        self.assertGreaterEqual(5, 4)

    def tearDown(self) -> None:
        print('teardown')


if __name__ == '__main__':
    unittest.main()
