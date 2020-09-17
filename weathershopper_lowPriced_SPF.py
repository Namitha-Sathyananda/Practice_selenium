'''
SCOPE:
1) Launch Chrome driver
2) Navigate to https://weathershopper.pythonanywhere.com/
3) take input from the console to particular type of moisturizer
4) Navigate to Sunscreen page
5) check the product containing perticular element (SFP-30/SFP-50)
6) compare the price for the lowest priced product.
7) Add to cart
6) Close the browser
'''



import time
from selenium import webdriver
from re import search

def lowest(price_list):
    "fetch the lowest amount product"
    low_price = min(price_list)
    #min_index = price_list.index(low_price)
    return low_price


def sunscreen_spf(spf):
    "select lowest priced product according to the SFP of the sunscreen."
    product = []
    price =[]
    browser.find_element_by_xpath('//a[@href = "/sunscreen"]').click()

    add_button = browser.find_elements_by_xpath('//button[@class = "btn btn-primary"]')
    for each_button in add_button:
        details = each_button.get_attribute("onclick")
        print(details)
    # checking for the "SPF-30/SPF-50" word in the string
        if search(spf,details):
            product.append(details.split("'")[1:-1][0])
            price.append(int(details.split(",")[1].strip(")")))

    # passing list of price to lowest function and fetching the result and its index
    lowest_Product = lowest(price)
    index_min = price.index(lowest_Product)
    
    # getting product name for the corresponding index
    low_priced_sunscreen = product[index_min]
    print("\n",low_priced_sunscreen,lowest_Product,"\n")
    low_priced_sunscreen ="'"+ low_priced_sunscreen +"'"

    browser.find_element_by_xpath('//button[@onclick ="addToCart(%s,%s)"]'%(low_priced_sunscreen,str(lowest_Product))).click()
    return

# getting the input from the console to check for SPF-30 or SPF-50 product.
sunscreen = input("Enter the type of sunscreen (SPF-30 or SPF-50):  \n")
    
browser = webdriver.Chrome()
browser.get("https://weathershopper.pythonanywhere.com/")

# passing the input from the console to the moisturizer_type function.
sunscreen_spf(sunscreen)


time.sleep(5)
browser.quit()