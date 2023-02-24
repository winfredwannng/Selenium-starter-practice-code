import unittest
from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By


class BaiduPage:
    def __init__(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()

        self.input_elem = (By.ID, 'kw')
        self.search_btn = (By.ID, 'su')

    def goto_baidu(self, url):
        self.driver.get(url)

    def search(self, url, kw):
        self.goto_baidu(url)
        self.driver.find_element(*self.input_elem).send_keys(kw)
        self.driver.find_element(*self.search_btn).click()
        sleep(3)


class TestBaidu(unittest.TestCase):
    def setUp(self) -> None:
        self.baiduPage = BaiduPage()

    def test_search(self):
        self.baiduPage.search('https://www.baidu.com', 'selenium')


if __name__ == '__main__':
    unittest.main()
