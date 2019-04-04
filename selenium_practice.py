from selenium import webdriver
driver = webdriver.Chrome()
driver.get('http://www.google.com')
#webdriver.Chrome().get('http://www.google.com')
element = driver.find_element_by_name('q')
element.send_keys('test')
from selenium.webdriver.common.keys import Keys
element.send_keys(Keys.ENTER)