import pickle
import random
import string
import time

from selenium.webdriver.common.by import By

from util import ddddocrutil
from PIL import Image
import os


# 识别图片验证码
def get_code(driver, id):
    t = time.time()
    path = os.path.dirname(os.path.dirname(__file__)) + '\\screenshots'
    picture_name1 = path + '\\' + str(t) + '.png'

    driver.save_screenshot(picture_name1)

    ce = driver.find_element(By.ID, id)

    left = ce.location['x']
    top = ce.location['y']
    right = ce.size['width'] + left
    height = ce.size['height'] + top

    im = Image.open(picture_name1)
    img = im.crop((left, top, right, height))

    t = time.time()

    picture_name2 = path + '\\' + str(t) + '.png'
    img.save(picture_name2)

    code = ddddocrutil.img2text(picture_name2)
    return code


# 生成随机字符串
def gen_random_str():
    rand_str = ''.join(random.sample(string.ascii_letters + string.digits, 8))
    return rand_str


def save_cookie(driver, path):
    with open(path, 'wb') as filehandler:
        cookies = driver.get_cookies()
        print(cookies)
        pickle.dump(cookies, filehandler)


def load_cookie(driver, path):
    with open(path, 'rb') as cookiesfile:
        cookies = pickle.load(cookiesfile)
        for cookie in cookies:
            driver.add_cookie(cookie)


def get_logger():
    """logging日志"""

    import logging.handlers
    import datetime

    # 获得一个logger 名字叫mylogger
    logger = logging.getLogger('mylogger')
    logger.setLevel(logging.DEBUG)  # 设置级别
    # 放在同目录logs目录里
    path = os.path.dirname(os.path.dirname(__file__)) + '/logs'
    data = time.strftime('%Y%m%d%H%M', time.localtime())

    # 根据时间，将日志消息放在磁盘中
    # atTime时间设置成，当前日期凌晨，这个没有测试，atTime参数是这个时间就发送？待...
    # when 是按照什么日期切分
    # interval 间隔1
    # backupCount 日志保留7个
    date = datetime.datetime.now()
    zero_time = datetime.datetime(date.year, date.month, date.day, 0, 0, 0)

    filename = path + '/all_' + data + '.log'
    rf_handler = logging.handlers.TimedRotatingFileHandler(
        filename=filename, when='midnight', interval=1, backupCount=7,
        encoding='utf-8', atTime=zero_time)

    # 设置日志格式
    rf_handler.setFormatter(logging.Formatter("%(asctime)s -%(name)s- %(levelname)s - %(message)s"))

    # 创建一个handler写错误级别的日志
    f_handler = logging.FileHandler(path + '/error_' + data + '.log', encoding='utf8')
    f_handler.setLevel(logging.ERROR)
    f_handler.setFormatter(
        logging.Formatter("%(asctime)s -%(name)s- %(levelname)s - %(filename)s[:%(lineno)d] - %(message)s"))

    # # 创建输出到控制台的hadler
    # console=logging.StreamHandler()
    #
    # # 将logger添加handler

    logger.addHandler(rf_handler)
    logger.addHandler(f_handler)

    # logger.addHandler(console)

    return logger
