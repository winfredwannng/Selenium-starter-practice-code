import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from PIL import Image
import pyautogui
import util.ddddocrutil


def test1():
    browser = webdriver.Chrome()
    browser.get('http://localhost:8080/user/login')
    browser.maximize_window()

    t = time.time()
    picture_name1 = str(t) + '.png'
    browser.save_screenshot(picture_name1)

    ce = browser.find_element(By.ID, 'captcha-img')
    print(ce.location)
    print(pyautogui.position())
    left = ce.location['x']
    top = ce.location['y']
    print(left,top)
    right = ce.size['width'] + left
    height = ce.size['height'] + top

    im = Image.open(picture_name1)
    img = im.crop((left, top, right, height))

    t = time.time()
    picture_name2 = str(t) + '.png'

    img.save(picture_name2)
    browser.close()

def test2():
    img = '1676893640.8535852.png'
    util.ddddocrutil.img2text(img)