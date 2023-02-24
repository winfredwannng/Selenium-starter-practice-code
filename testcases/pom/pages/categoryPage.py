from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

from testcases.pom.basePage import BasePage

class CategoryPage(BasePage):
    def __init__(self, driver):
        BasePage.__init__(self, driver)

    click_article_loc = (By.XPATH, '//*[@id="group-article"]/a')
    click_article_category_loc = (By.XPATH, '//*[@id="分类--/admin/article/category"]/a/p')
    category_name_loc = (By.NAME, 'category.title')
    parent_category_loc = (By.NAME, 'category.pid')
    slug_loc = (By.NAME, 'category.slug')
    add_btn_loc = (
            By.XPATH, '/html/body/div/div[1]/section[2]/div/div[1]/div/form/div[2]/div/div/button')

    def click_article(self):
        self.click(*self.click_article_loc)

    def click_article_category(self):
        self.click(*self.click_article_category_loc)

    def input_category_name(self, name):
        self.input_text(name, *self.category_name_loc)

    def select_parent_category(self, parent_name):
        parent_category_elem = self.find_element(*self.parent_category_loc)
        Select(parent_category_elem).select_by_visible_text(parent_name)

    def input_slug(self, slug):
        self.input_text(slug, *self.slug_loc)

    def click_add(self):
        self.click(*self.add_btn_loc)


