'''
SCOPE:
1) Launch Chrome driver
2) Navigate to https://weathershopper.pythonanywhere.com/
3) validate the title.
3) check for the temperature.
4) navigate to moisturiser page if the temperature is below 19
5) navigate to sunscreen page if the temperature is above 35
6) Close the browser
'''

import time
from selenium import webdriver

browser = webdriver.Chrome()
browser.get("https://weathershopper.pythonanywhere.com/")

if (browser.title == "Current Temperature"):
    print("successful navigation to the right page")
else:
    print(" Please check the URL again")

    
time.sleep(3)

# strore the value to a variable 
temperature = browser.find_element_by_id("temperature").text
# get the substring and coverting it to interger data type.
value_temperature = int(temperature.split(" ")[0])

# compare the temperature and navigate to the right page.
if value_temperature < 19:
    browser.find_element_by_xpath('//a[@href="/moisturizer"]').click()
elif value_temperature > 34:
    browser.find_element_by_xpath('//a[@href="/sunscreen"]').click()
else:
    print("Nothing to shop for this weather")

time.sleep(3)


browser.quit()