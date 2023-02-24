from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from util import util
import pytest


class TestUserLogin:

    def setup_class(self):
        self.driver = webdriver.Chrome()
        self.driver.get('http://localhost:8080/user/login')
        self.driver.maximize_window()
        self.logger = util.get_logger()
        self.logger.info('start test....')

    def test_user_login_username_error(self):
        username = ''
        pwd = '123456'
        expected = '这是必填内容'

        self.driver.find_element(By.NAME, 'user').clear()
        self.driver.find_element(By.NAME, 'user').send_keys(username)
        self.logger.debug('input username: %s', username)

        self.driver.find_element(By.NAME, 'pwd').clear()
        self.driver.find_element(By.NAME, 'pwd').send_keys(pwd)
        self.logger.debug('input password: %s', pwd)

        self.driver.find_element(By.NAME, 'captcha').clear()
        code = util.get_code(self.driver, 'captcha-img')
        self.driver.find_element(By.NAME, 'captcha').send_keys(code)
        self.logger.debug('input captcha: %s', code)

        self.driver.find_element(By.CLASS_NAME, 'btn').click()
        user_error = self.driver.find_element(By.ID, 'user-error')
        WebDriverWait(self.driver, 5).until(EC.presence_of_element_located((By.ID, 'user-error')))
        sleep(3)

        try:
            assert user_error.text == expected
        except AssertionError as ae:
            self.logger.error('assert error!', exc_info=1)

    def test_user_login_username_ok(self):
        username = 'admin'
        pwd = '123456'
        expected = '用户中心'

        self.driver.find_element(By.NAME, 'user').clear()
        self.driver.find_element(By.NAME, 'user').send_keys(username)
        self.logger.debug('input username: %s', username)

        self.driver.find_element(By.NAME, 'pwd').clear()
        self.driver.find_element(By.NAME, 'pwd').send_keys(pwd)
        self.logger.debug('input password: %s', pwd)

        self.driver.find_element(By.NAME, 'captcha').clear()
        code = util.get_code(self.driver, 'captcha-img')
        self.driver.find_element(By.NAME, 'captcha').send_keys(code)
        self.logger.debug('input captcha: %s', code)

        self.driver.find_element(By.CLASS_NAME, 'btn').click()
        self.logger.debug('login...')
        WebDriverWait(self.driver, 5).until(EC.title_is(expected))
        sleep(3)

        try:
            assert self.driver.title == expected
        except AssertionError as ae:
            self.logger.error('assert error!', exc_info=1)


if __name__ == '__main__':
    pytest.main(['-sv', 'test_user_login.py'])
