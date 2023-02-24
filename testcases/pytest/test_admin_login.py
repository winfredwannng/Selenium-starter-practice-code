import pytest

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from util import util
from time import sleep
import warnings


class TestAdminLogin:
    data = [('admin', '123456', '6666', '验证码不正确，请重新输入'),
            ('admin', '123456', '7777', 'JPress后台')]

    def setup_class(cls):
        cls.driver = webdriver.Chrome()
        cls.driver.get('http://localhost:8080/admin/login')
        cls.driver.maximize_window()
        cls.logger = util.get_logger()
        cls.logger.info('start test...')
        warnings.simplefilter('ignore', ResourceWarning)
        sleep(2)

    @pytest.mark.dependency(name='admin_login')
    @pytest.mark.parametrize('username,pwd,captcha,expected', data)
    def test_admin_login_code(self, username, pwd, captcha, expected):
        # username = 'admin'
        # pwd = '123456'
        # captcha = '6666'
        # expected = '验证码不正确，请重新输入'
        self.driver.find_element(By.NAME, 'user').clear()
        self.driver.find_element(By.NAME, 'user').send_keys(username)
        self.logger.info('input username:%s', username)

        self.driver.find_element(By.NAME, 'pwd').clear()
        self.driver.find_element(By.NAME, 'pwd').send_keys(pwd)
        self.logger.info('input pwd:%s', pwd)

        if captcha == '6666':

            self.driver.find_element(By.NAME, 'captcha').clear()
            self.driver.find_element(By.NAME, 'captcha').send_keys(captcha)
            self.logger.info('input captcha:%s', captcha)
            self.driver.find_element(By.CLASS_NAME, 'btn').click()
            self.logger.info('login...')

            WebDriverWait(self.driver, 5).until(EC.alert_is_present())
            alert = self.driver.switch_to.alert
            try:
                assert alert.text == expected
            except AssertionError as ae:
                self.logger.error('assert error!', exc_info=1)
            alert.accept()
            sleep(2)
        else:
            captcha = util.get_code(self.driver, 'captcha-img')
            self.driver.find_element(By.NAME, 'captcha').send_keys(captcha)
            self.logger.info('input captcha:%s', captcha)
            self.driver.find_element(By.CLASS_NAME, 'btn').click()
            self.logger.info('login...')

            WebDriverWait(self.driver, 5).until(EC.title_is(expected))
            try:
                assert expected == self.driver.title
            except AssertionError as ae:
                self.logger.error('assert error!', exc_info=1)


if __name__ == '__main__':
    pytest.main(['test_admin_login.py'])
