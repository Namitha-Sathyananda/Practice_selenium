import time
from selenium import webdriver
from re import search

browser = webdriver.Chrome()
browser.get("https://weathershopper.pythonanywhere.com/")

browser.find_element_by_xpath('//a[@href="/moisturizer"]').click()

# To get all the products names into a list
product_list = []
aloe_list = []
aloe_list_index = []
product = browser.find_elements_by_xpath('//div[@class = "text-center col-4"]//p[1]')
for each_product in product:
    product_list.append(each_product.text)

for each in product_list:
    if search("Aloe",each):
        aloe_list.append(each)
        aloe_index= product_list.index(each)
        aloe_list_index.append(aloe_index)

print(aloe_list)
print(aloe_list_index)
'''
# To get all the corresponding products price into a list
price_list =[]
price = browser.find_elements_by_xpath('//div[@class = "text-center col-4"]//p[2]')
for each_price in price:
    price_num = each_price.text
    num = price_num.rsplit(' ',1)[-1]
    listOfInt = int(num.split("\n")[0])
    price_list.append(listOfInt)


# Checking product that is of low price.
low_price = min(price_list)
min_index = price_list.index(low_price)

# getting product name for the corresponding index
low_priced_moisturiser = product_list[min_index]
low_priced_moisturiser = "'"+ low_priced_moisturiser +"'"
print(low_priced_moisturiser)


browser.find_element_by_xpath('//button[@onclick ="addToCart(%s,%s)"]'%(low_priced_moisturiser,str(low_price))).click()

''' 
time.sleep(3)

browser.quit()