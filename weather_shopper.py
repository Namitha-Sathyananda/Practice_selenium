'''
SCOPE:
1) Launch Chrome driver
2) Navigate to https://weathershopper.pythonanywhere.com/
3) validate the title.
3) check for the temperature.
4) navigate to moisturiser page if the temperature is below 19
5) navigate to sunscreen page if the temperature is above 35
6) Add all the products in the cart on the navigated page 
7) Check wheather cart contains all the products.
8) Close the browser
'''

import time
from selenium import webdriver

browser = webdriver.Chrome()
browser.get("https://weathershopper.pythonanywhere.com/")

if (browser.title == "Current Temperature"):
    print("successful navigation to current weather page")
else:
    print(" Please check the URL again")

add = []   

time.sleep(3)

# strore the value to a variable 
temperature = browser.find_element_by_id("temperature").text
# get the substring and coverting it to interger data type.
value_temperature = int(temperature.split(" ")[0])

# compare the temperature and navigate to the right page.
if value_temperature < 19:
    browser.find_element_by_xpath('//a[@href="/moisturizer"]').click()

# Checking for the right page landing for the moisturizer
    if browser.title == "The Best Moisturizers in the World!":
       print("successful navigation to the Moisturizer page")

# click all the Add button
       add = (browser.find_elements_by_xpath('//button[@class="btn btn-primary"]'))
       for all in add:
           all.click()

    else:
        print(" Please check the Moisturizer page URL again")
    
elif value_temperature > 34:
    browser.find_element_by_xpath('//a[@href="/sunscreen"]').click()

# Checking for the right page landing for the sunscreen
    if browser.title == "The Best Sunscreens in the World!":
        print("successful navigation to the Sunscreen shopping page")

# click all the Add button
        add = (browser.find_elements_by_xpath('//button[@class="btn btn-primary"]'))
        for all in add:
            all.click()

    else:
        print(" Please check the shopping page URL again")

else:
    print("Nothing to shop for this weather")

# check the cart for all the products
no_of_products = browser.find_element_by_id("cart").text
total = int(no_of_products.split(" ")[0])

if total == 6 and value_temperature < 19:
    print("All moisturizers added")

elif total == 6 and value_temperature > 34:
    print("All sunscreens added")
    
else:
    print("few products missing")

time.sleep(3)
browser.quit()