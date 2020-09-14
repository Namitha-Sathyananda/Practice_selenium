import time

from selenium import webdriver

browser = webdriver.Chrome()
browser.get("https://weathershopper.pythonanywhere.com/")

browser.find_element_by_xpath('//a[@href="/moisturizer"]').click()

product_list = []
product = browser.find_elements_by_xpath('//div[@class = "text-center col-4"]//p[1]')
for i in product: 
    pro_names = i.text
    list = pro_names.split("\n")
    product_list.append(list)

print(product_list)


price_list =[]
price = browser.find_elements_by_xpath('//div[@class = "text-center col-4"]//p[2]')
for i in price:
    price_num = i.text
    num = price_num.rsplit(' ',1)[-1]
    list = int(num.split("\n")[0])
    price_list.append(list)


print(price_list)

low_price = min(price_list)
min_index = price_list.index(low_price)
print(min_index)

moist =str(product_list[min_index])[2:-2]
print(moist)
time.sleep(3)

b = browser.find_element_by_xpath('//button[@onclick = "addToCart("'%s'","%s'")"]'%(moist,low_price)).click()


print(b)
 
time.sleep(3)

browser.quit()