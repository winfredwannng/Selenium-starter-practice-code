import unittest
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from util import util


class TestUserLogin(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        cls.driver = webdriver.Chrome()
        cls.driver.get('http://localhost:8080/user/login')
        cls.driver.maximize_window()

    # def __init__(self):
    #     self.driver = webdriver.Chrome()
    #     self.driver.get('http://localhost:8080/user/login')
    #     self.driver.maximize_window()

    def test_user_login_username_error(self):
        username = ''
        pwd = '123456'
        expected = '这是必填内容'

        self.driver.find_element(By.NAME, 'user').clear()
        self.driver.find_element(By.NAME, 'user').send_keys(username)

        self.driver.find_element(By.NAME, 'pwd').clear()
        self.driver.find_element(By.NAME, 'pwd').send_keys(pwd)

        self.driver.find_element(By.NAME, 'captcha').clear()
        code = util.get_code(self.driver, 'captcha-img')
        self.driver.find_element(By.NAME, 'captcha').send_keys(code)

        self.driver.find_element(By.CLASS_NAME, 'btn').click()
        user_error = self.driver.find_element(By.ID, 'user-error')
        WebDriverWait(self.driver, 5).until(EC.presence_of_element_located((By.ID, 'user-error')))
        sleep(3)

        self.assertEqual(user_error.text, expected)

    def test_user_login_username_ok(self):
        username = 'admin'
        pwd = '123456'
        expected = '用户中心'

        self.driver.find_element(By.NAME, 'user').clear()
        self.driver.find_element(By.NAME, 'user').send_keys(username)

        self.driver.find_element(By.NAME, 'pwd').clear()
        self.driver.find_element(By.NAME, 'pwd').send_keys(pwd)

        self.driver.find_element(By.NAME, 'captcha').clear()
        code = util.get_code(self.driver, 'captcha-img')
        self.driver.find_element(By.NAME, 'captcha').send_keys(code)

        self.driver.find_element(By.CLASS_NAME, 'btn').click()
        WebDriverWait(self.driver, 5).until(EC.title_is(expected))
        sleep(3)

        self.assertEqual(self.driver.title,expected)

if __name__ == '__main__':
    unittest.main()

