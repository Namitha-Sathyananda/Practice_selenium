'''
SCOPE:
1) Launch Chrome driver
2) Navigate to http://qainterview.pythonanywhere.com/
3) Fill all the text field
4) Click on Calcutate button
5) Validate the result.
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


def moisturizer_type(moist):
    "select lowest priced product according to the ingredient in moisturizer."
    product = []
    price =[]
    browser.find_element_by_xpath('//a[@href = "/moisturizer"]').click()

    add_button = browser.find_elements_by_xpath('//button[@class = "btn btn-primary"]')
    for each_button in add_button:
        details = each_button.get_attribute("onclick")
        print(details)
    # checking for the "Aloe or Almond" word in the string
        if search(moist,details):
            product.append(details.split("'")[1:-1][0])
            price.append(int(details.split(",")[1].strip(")")))

    # passing list of price to lowest function and fetching the result and its index
    lowest_Product = lowest(price)
    index_min = price.index(lowest_Product)
    
    # getting product name for the corresponding index
    low_priced_moisturiser = product[index_min]
    print("\n",low_priced_moisturiser,lowest_Product,"\n")
    low_priced_moisturiser ="'"+ low_priced_moisturiser +"'"
    
    browser.find_element_by_xpath('//button[@onclick ="addToCart(%s,%s)"]'%(low_priced_moisturiser,str(lowest_Product))).click()


# getting the input from the console to check for Aloe or Almond producd.
moisturizer = input("Enter the ingredient in moisturiser (Aloe or Almond):  ")
    
browser = webdriver.Chrome()
browser.get("https://weathershopper.pythonanywhere.com/")

# passing the input from the console to the moisturizer_type function.
moisturizer_type(moisturizer)

time.sleep(5)
browser.quit()