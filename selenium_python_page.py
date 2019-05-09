from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
import time
# Defining the driver with the Chrome browser
driver = webdriver.Chrome()
driver.get('https://wiki.python.org/moin/FrontPage')
search_box = driver.find_element_by_id('searchinput')
search_box.clear()
search_box.send_keys('python tutorial')
search_submit = driver.find_element_by_id('fullsearch')
search_submit.send_keys(Keys.ENTER)
time.sleep(3)
select = Select(driver.find_element_by_xpath('//*/form/div/select'))
select.select_by_visible_text('Raw Text')
time.sleep(5)
driver.close()