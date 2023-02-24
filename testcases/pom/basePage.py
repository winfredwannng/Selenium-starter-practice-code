from time import sleep

from selenium.webdriver.common.by import By
from selenium import webdriver


class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def open(self, url=None):
        if url is None:
            self.driver.get(self.url)
        else:
            self.driver.get(url)

    def get_elem(self, *loc):
        return self.driver.find_element(*loc)

    def input_text(self, text, *loc):
        self.driver.find_element(*loc).send_keys(text)

    def click(self, *loc):
        self.driver.find_element(*loc).click()

    def get_title(self):
        return self.driver.title

    def get_text(self, xpath):
        return self.get_elem((By.XPATH, xpath)).text()

    def clear(self, *loc):
        self.driver.find_element(*loc).clear()

    def js(self, script):
        self.driver.execute_script(script)


class BaiduPage(BasePage):
    def __init__(self, driver):
        BasePage.__init__(self, driver)
        driver.get('https://www.baidu.com')
        sleep(2)

    def test_search(self):
        kw_loc = (By.ID, 'kw')
        search_btn_loc = (By.ID, 'su')
        self.input_text('selenium', *kw_loc)
        self.click(*search_btn_loc)
        sleep(2)


if __name__ == '__main__':
    driver = webdriver.Chrome()
    baiduPage = BaiduPage(driver)
    baiduPage.test_search()
