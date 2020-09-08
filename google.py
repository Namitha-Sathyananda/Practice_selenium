import time
from selenium import webdriver

browser = webdriver.Chrome()

browser.get('https://www.google.com/')

if(browser.title == "Google"):
    print("SUCCESS")
else:
    print("FAILURE")

search = browser.find_element_by_xpath("//input[@name='q']")
search.send_keys("Qxf2 services")
time.sleep(3)

select = browser.find_element_by_xpath("//input[@aria-label ='Google Search']").click()

time.sleep(5)

browser.close()




