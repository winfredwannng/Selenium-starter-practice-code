from selenium import webdriver
from time import sleep

from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class TestArticle:
    def __init__(self, login):
        self.login = login

    def test_add_ok(self):
        title = 'test'
        content = 'test content'
        expected = '文章保存成功。'

        # self.login.driver = webdriver.Chrome()
        self.login.driver.find_element(By.XPATH, '//*[@id="group-article"]/a').click()
        sleep(1)
        self.login.driver.find_element(By.XPATH, '//*[@id="写文章--/admin/article/write"]').click()
        sleep(1)

        self.login.driver.find_element(By.NAME, 'article.title').send_keys(title)
        self.login.driver.find_element(
            By.XPATH, '//*[@id="form"]/div/div[1]/div/div/div/div[2]/div[2]/div/p').send_keys(content)

        self.login.driver.find_element(By.XPATH, '//*[@id="form"]/section/div[2]/button[2]').click()
        toast_loc = (By.CLASS_NAME, 'toast-message')
        WebDriverWait(self.login.driver, 5).until(EC.presence_of_element_located(toast_loc))
        text = self.login.driver.find_element(*toast_loc).text

        assert text == expected

    def test_delete_ok(self):
        # self.login.driver = webdriver.Chrome()
        self.login.driver.find_element(By.XPATH, '//*[@id="group-article"]/a').click()
        sleep(1)
        self.login.driver.find_element(By.XPATH, '//*[@id="文章管理--/admin/article/list"]/a/p').click()
        sleep(1)

        link = self.login.driver.find_element(
            By.XPATH,'/html/body/div[1]/div[1]/section[2]/div/div/div[2]/table/tbody/tr[1]/td[3]/strong/a')
        ActionChains(self.login.driver).move_to_element(link).perform()
        sleep(2)

        article_num = int((self.login.driver.find_element(
            By.XPATH,'/html/body/div[1]/div[1]/section[1]/div/div/div[1]/div[2]/div/a[2]')).text.split('(')[1].split(')')[0])
        sleep(2)
        self.login.driver.find_element(
            By.XPATH,'/html/body/div[1]/div[1]/section[2]/div/div/div[2]/table/tbody/tr[1]/td[3]/div/div/a[3]').click()
        sleep(1)
        article_num_del = int((self.login.driver.find_element(
            By.XPATH,'/html/body/div[1]/div[1]/section[1]/div/div/div[1]/div[2]/div/a[2]')).text.split('(')[1].split(')')[0])

        assert article_num == article_num_del + 1
