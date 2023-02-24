from selenium import webdriver
from selenium.webdriver import ChromeOptions

chromeOptions = ChromeOptions()

driver = webdriver.Remote("http://localhost:4444/wd/hub", options=chromeOptions)
driver.get("https://www.baidu.com")
print(driver.title)
