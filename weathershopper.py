import time
import random
import string
from re import search
from selenium import webdriver


def lowest(price_list):
    "fetch the lowest amount product"
    low_price = min(price_list)
    #min_index = price_list.index(low_price)
    return low_price


def low_price_product(item):
    "select lowest priced product according to the requirement."
    product = []
    price =[]
    
    add_button = browser.find_elements_by_xpath('//button[contains(@class,"btn btn-primary")]')
    for each_button in add_button:
        details = each_button.get_attribute("onclick")
    # checking for the "SPF-30/SPF-50" word in the string
        if search(item,details):
            product.append(details.split("'")[1:-1][0])
            price.append(int(details.split(",")[1].strip(")")))

    # passing list of price to lowest function and fetching the result and its index
    lowest_Product = lowest(price)
    index_min = price.index(lowest_Product)
    
    # getting product name for the corresponding index
    low_priced_item = product[index_min]
    print(f"\n Lowest priced product in {item} is {low_priced_item}, Rs {lowest_Product},\n")
    low_priced_item ="'"+ low_priced_item +"'"

    browser.find_element_by_xpath('//button[@onclick ="addToCart(%s,%s)"]'%(low_priced_item,str(lowest_Product))).click()

def payment():
    " takes the details of the credit or debit card and checks the payment successful or not"
    browser.find_element_by_xpath('//button[@type="submit"]').click()
    time.sleep(3)
    iframe = browser.find_element_by_xpath("//iframe[contains(@name,'stripe_checkout_app')]")
    browser.switch_to_frame(iframe)
    user = ''.join(random.choice(string.ascii_letters+string.digits)for i in range(4))
    user_id = user + '@gmail.com'
    email = browser.find_element_by_xpath('//input[@inputmode = "email"]')
    email.send_keys(user_id)
    card_number = browser.find_element_by_xpath('//input[@placeholder="Card number"]')
    card_number.send_keys("4242424242424242")
    time.sleep(2)
    expiery_date = browser.find_element_by_xpath('//input[@placeholder = "MM / YY"]')
    expiery_date.send_keys("10/20")
    CVC = browser.find_element_by_xpath('//input[@placeholder = "CVC"]')
    CVC.send_keys("334")
    zip_code = browser.find_element_by_xpath('//input[@placeholder = "ZIP Code"]')
    zip_code.send_keys("572103")
    browser.find_element_by_xpath('//a[@href= "#"]').click()
    mobile_number = browser.find_element_by_xpath('//input[@inputmode = "tel"]')
    mobile_number.send_keys("9784563364")
    time.sleep(2)
    browser.find_element_by_xpath('//div[@class="Section-button"]/button').click()
    browser.switch_to_default_content()
    time.sleep(10)
    message = browser.find_element_by_xpath('//h2').text
    print('\n', message) 

def cart_items():
    "Checks the total amout in the cart"
    name = []
    price = []
    table = browser.find_element_by_xpath('//table[@class ="table table-striped"]')
    cart_items = table.find_elements_by_xpath("//tbody/descendant::tr")

    for every_tr in cart_items:
        product_name = every_tr.find_element_by_xpath('.//td[1]').text
        name.append(product_name)
        product_price = every_tr.find_element_by_xpath(".//td[2]").text
        price.append(int(product_price))

    total_amt = sum(price)

    total = browser.find_element_by_id("total").text
    amt = int(total.split(' ')[-1])
    if total_amt == amt:
        print("\n Amount matched \n")
        payment()
    else:
        print("\n Amount mismatch \n")



if __name__ == "__main__":

    browser = webdriver.Chrome()
    browser.get("https://weathershopper.pythonanywhere.com/")

    if (browser.title == "Current Temperature"):
        print("successful navigation to current weather page")
    else:
        print(" Please check the URL again")
    
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
            sub_element = ['Aloe','Almond']
            for each_condition in sub_element:
                low_price_product(each_condition)

            
    elif value_temperature > 34:
        browser.find_element_by_xpath('//a[@href="/sunscreen"]').click()

# Checking for the right page landing for the sunscreen
        if browser.title == "The Best Sunscreens in the World!":
            print("successful navigation to the Sunscreen shopping page")

            Spf =['SPF-30','SPF-50']
            for each_condition in Spf:
                low_price_product(each_condition)

    browser.find_element_by_xpath('//button[@onclick ="goToCart()"]').click()
    
    # navigate to cart page.
    cart_items()

    time.sleep(2)
    browser.quit()