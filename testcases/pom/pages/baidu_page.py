from selenium.webdriver.common.by import By

from testcases.pom.basePage import BasePage
from poium import Page
from poium import Element

class BaiduPage(BasePage):
    url = 'https://www.baidu.com'
    search_field = Element(id_='kw')
    search_btn = Element(id_='su')

    # def search_input(self, search_key):
    #     self.get_elem(*self.search_field).send_keys(search_key)

    # def search_button(self):
    #     # search_btn = (By.ID, 'su')
    #     self.get_elem(*self.search_btn).click()
