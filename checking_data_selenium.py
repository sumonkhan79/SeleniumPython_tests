from selenium import webdriver
driver = webdriver.Chrome()
driver.get('https://www.phptravels.net/offers')
b_tags = driver.find_elements_by_tag_name('b')
offer_list = []
for b in b_tags:
    offer_list.append(b.text)
print(offer_list)
clean_price_list =[]
for price in offer_list:
    if price.startswith('USD'):
        number = price[5:]
        number_price=int(number.replace(',',''))
        clean_price_list.append(number_price)
print(sorted(clean_price_list))