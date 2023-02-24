import allure
import pytest


@pytest.fixture(scope='session')
def login():
    print('login first')


@allure.step('step1:click xxx')
def step_1():
    print('111')


@allure.step('step2:click xxx')
def step_2():
    print("222")


@allure.feature('edit page')
class TestEditPage():

    @allure.story('this is a case of xxx')
    def test_1(self, login):
        step_1()
        step_2()
        print("xxx")

    @allure.story("open page A")
    def test_2(self, login):
        print("yyy")


if __name__ == '__main__':
    pytest.main(['--alluredir', './reports', 'test08.py'])
    pytest.main(['--alluredir', './reports', 'test08.py'])
