from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select
from time import sleep
import pytest

from util import util
from testcases.pytest.test_admin_login import TestAdminLogin


class TestCategory:
    data = [('', 'python', 'test', '这是必填内容'),
            ('test', 'python', 'test', '文章分类保存成功')]

    def setup_class(self):
        self.login = TestAdminLogin()
        self.logger = util.get_logger()
        self.logger.info('start testing ...')

    @pytest.mark.dependency(depends=["admin_login"], scope="module")
    @pytest.mark.parametrize('name,parent,slug,expected', data)
    def test_add_category(self, name, parent, slug, expected):
        if name == '':
            self.login.driver.find_element(By.XPATH, '//*[@id="group-article"]/a').click()

        cateloc = (By.XPATH, '//*[@id="分类--/admin/article/category"]/a/p')
        sleep(2)
        self.login.driver.find_element(*cateloc).click()
        self.logger.debug('click category...')

        self.login.driver.find_element(By.NAME, 'category.title').clear()
        self.login.driver.find_element(By.NAME, 'category.title').send_keys(name)
        self.logger.debug('input name...')

        parent_category_elem = self.login.driver.find_element(By.NAME, 'category.pid')
        Select(parent_category_elem).select_by_visible_text(parent)

        self.login.driver.find_element(By.NAME, 'category.slug').clear()
        self.login.driver.find_element(By.NAME, 'category.slug').send_keys(slug)
        self.logger.debug('input slug...')

        self.login.driver.find_element(
            By.XPATH, '/html/body/div/div[1]/section[2]/div/div[1]/div/form/div[2]/div/div/button').click()
        if name == '':
            title_error_loc = (By.ID, 'category.title-error')
            WebDriverWait(self.login.driver, 5).until(EC.presence_of_element_located(title_error_loc))

            msg = self.login.driver.find_element(*title_error_loc).text
            assert msg == expected
        else:
            title_ok_loc = (By.CLASS_NAME, 'toast-message')
            WebDriverWait(self.login.driver, 5).until(EC.presence_of_element_located(title_ok_loc))

            msg = self.login.driver.find_element(*title_ok_loc).text
            assert msg == expected


if __name__ == '__main__':
    pytest.main(['test_category.py'])
