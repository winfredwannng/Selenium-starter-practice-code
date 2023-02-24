import unittest
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from testcases.pom.pages.baidu_page import BaiduPage


class TestBaidu(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.driver = webdriver.Chrome()

    def test_baidu_search_case(self):
        page = BaiduPage(self.driver)
        page.open()
        sleep(2)
        page.search_input('selenium')
        page.search_button()
        sleep(2)
        self.assertEqual(page.get_title(), 'selenium_百度搜索')

    def test_baidu_search_case1(self):
        page = BaiduPage(self.driver)
        page.open()
        sleep(2)
        page.search_field.send_keys('selenium')
        page.search_btn.click()
        sleep(2)
        self.assertEqual(page.get_title(), 'selenium_百度搜索')

    @classmethod
    def tearDownClass(cls) -> None:
        cls.driver.quit()


if __name__ == '__main__':
    unittest.main(verbosity=2)
