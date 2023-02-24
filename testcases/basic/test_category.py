from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select
from time import sleep


class TestCategory:
    def __init__(self, login):
        self.login = login

    def test_add_category_error(self):
        name = ''
        parent = 'python'
        slug = 'test'
        expected = '这是必填内容'

        # self.login.driver = webdriver.Chrome()
        # self.login.driver.get('http://localhost:8080/admin/index')
        self.login.driver.find_element(By.XPATH, '//*[@id="group-article"]/a').click()
        cateloc = (By.XPATH, '//*[@id="分类--/admin/article/category"]/a/p')
        # WebDriverWait(self.login.driver, 5).until(EC.presence_of_element_located(cateloc))
        sleep(2)
        self.login.driver.find_element(*cateloc).click()

        self.login.driver.find_element(By.NAME, 'category.title').send_keys(name)

        parent_category_elem = self.login.driver.find_element(By.NAME, 'category.pid')
        Select(parent_category_elem).select_by_visible_text(parent)

        self.login.driver.find_element(By.NAME, 'category.slug').send_keys(slug)

        self.login.driver.find_element(
            By.XPATH, '/html/body/div/div[1]/section[2]/div/div[1]/div/form/div[2]/div/div/button').click()

        title_error_loc = (By.ID, 'category.title-error')
        WebDriverWait(self.login.driver, 5).until(EC.presence_of_element_located(title_error_loc))

        msg = self.login.driver.find_element(*title_error_loc).text
        assert msg == expected

    def test_add_category_ok(self):
        name = 'test'
        parent = 'python'
        slug = 'test'
        expected = '文章分类保存成功'

        self.login.driver.find_element(By.XPATH, '//*[@id="group-article"]/a').click()
        cateloc = (By.XPATH, '//*[@id="分类--/admin/article/category"]/a/p')
        # WebDriverWait(self.login.driver, 5).until(EC.presence_of_element_located(cateloc))
        sleep(2)
        self.login.driver.find_element(*cateloc).click()

        self.login.driver.find_element(By.NAME, 'category.title').clear()
        self.login.driver.find_element(By.NAME, 'category.title').send_keys(name)

        parent_category_elem = self.login.driver.find_element(By.NAME, 'category.pid')
        Select(parent_category_elem).select_by_visible_text(parent)

        self.login.driver.find_element(By.NAME, 'category.slug').clear()
        self.login.driver.find_element(By.NAME, 'category.slug').send_keys(slug)

        self.login.driver.find_element(
            By.XPATH, '/html/body/div/div[1]/section[2]/div/div[1]/div/form/div[2]/div/div/button').click()

        title_ok_loc = (By.CLASS_NAME, 'toast-message')
        WebDriverWait(self.login.driver, 5).until(EC.presence_of_element_located(title_ok_loc))

        msg = self.login.driver.find_element(*title_ok_loc).text
        assert msg == expected
