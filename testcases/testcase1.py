from time import sleep
from selenium.webdriver.common.by import By
from selenium import webdriver
import pyautogui


def test1():
    print('test1')


def test2():
    driver = webdriver.Chrome()
    driver.get(
        'https://passport.baidu.com/v2/?reg&tt=1676888506234&overseas=undefined&gid=AC5C806-5995-4DC6-853C'
        '-8AF4B8EEB0E6&tpl=mn&u=https%3A%2F%2Fwww.baidu.com%2F%3Ftn%3D85070231_33_hao_pg')
    driver.maximize_window()
    sleep(3)
    elem = driver.find_element(By.NAME, 'isAgree')
    print(elem.rect)
    rect1 = elem.rect
    print(pyautogui.size())
    pyautogui.click(rect1['x'], rect1['y'])
    # pyautogui.click()
    sleep(2)
    e2 = driver.find_element(By.ID,'TANGRAM__PSP_4__phone')
    rect2 = e2.rect
    pyautogui.click(rect2['x'], rect2['y'])
    sleep(2)
    
