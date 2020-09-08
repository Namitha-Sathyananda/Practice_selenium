''' Navigate to specified url and check for the titile'''

import time
from selenium import webdriver

browser = webdriver.Chrome()

browser.get('http://qainterview.pythonanywhere.com/')
time.sleep(5)

if (browser.title == "Factoriall"):
    print("successful navigation with right title")
else:
    print("successful with wrong title")


browser.quit()
