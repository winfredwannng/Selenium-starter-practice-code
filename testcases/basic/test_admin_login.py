from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from util import util
from time import sleep


class TestAdminLogin:
    def __init__(self):
        self.driver = webdriver.Chrome()
        self.driver.get('http://localhost:8080/admin/login')
        self.driver.maximize_window()
        sleep(2)

    def test_admin_login_code_error(self):
        username = 'admin'
        pwd = '123456'
        captcha = '6666'
        expected = '验证码不正确，请重新输入'

        self.driver.find_element(By.NAME, 'user').send_keys(username)
        self.driver.find_element(By.NAME, 'pwd').send_keys(pwd)
        self.driver.find_element(By.NAME, 'captcha').send_keys(captcha)
        self.driver.find_element(By.CLASS_NAME, 'btn').click()

        WebDriverWait(self.driver, 5).until(EC.alert_is_present())
        alert = self.driver.switch_to.alert

        assert alert.text == expected
        alert.accept()

    def test_admin_login_code_ok(self):
        username = 'admin'
        pwd = '123456'
        expected = 'JPress后台'

        self.driver.find_element(By.NAME, 'user').clear()
        self.driver.find_element(By.NAME, 'user').send_keys(username)
        self.driver.find_element(By.NAME, 'pwd').clear()
        self.driver.find_element(By.NAME, 'pwd').send_keys(pwd)
        captcha = util.get_code(self.driver,'captcha-img')
        self.driver.find_element(By.NAME, 'captcha').send_keys(captcha)
        self.driver.find_element(By.CLASS_NAME, 'btn').click()

        WebDriverWait(self.driver, 5).until(EC.title_is(expected))

        assert expected == self.driver.title


