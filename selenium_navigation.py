from selenium import webdriver
driver = webdriver.Chrome()
driver.get('https://www.seleniumhq.org/')
element = driver.find_element_by_xpath('//*[@id="choice"]/tbody/tr/td[2]/center/a/img')
element.click()
driver.back()
search_element = driver.find_element_by_id('q')
search_element.send_keys('webdriver')
go_button= driver.find_element_by_id("submit")
go_button.click()
import time
time.sleep(5)
driver.switch_to.frame('master-1')
link_elements = driver.find_elements_by_tag_name('script')

print(link_elements[0].get_attribute('href'))