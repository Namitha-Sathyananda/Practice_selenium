''' 
SCOPE:
1) Launch Chrome driver
2) Navigate to http://qainterview.pythonanywhere.com/
3) Fill all the text field
4) Click on Calcutate button
5) Validate the result.
6) Close the browser
'''
import math
import time
import selenium
from selenium import webdriver

#Calulating the factorial of a number in python to compare the result with the factorial page 
number = 7
fact = math.factorial(number)

# Create an instance of IE WebDriver
browser = webdriver.Chrome()

# Navigate to Factoriall page.
browser.get('http://qainterview.pythonanywhere.com/')

# Check the title and print the  message to see the langing page is right or wrong.
if (browser.title == "Factoriall"):
    print("successful navigation with right title")
else:
    print("successful with wrong title")

# locate the placeholder throuht the Xpath and pass the value
browser.find_element_by_xpath('.//input[@placeholder="Enter an integer"]').send_keys(number)

# find submit button and click it
browser.find_element_by_xpath("//button[@type='submit']").click()
time.sleep(3)

# capture the result to a variable
result = browser.find_element_by_xpath("/html/body/div[1]/div[2]/div/p[@id='resultDiv']").text

# fetch the value needed from the string and convert to integer type
value = int(result.split(":")[1].lstrip())

#compare our result with the factorial website result and display the message
if(fact == value):
    print("Displaying right result")
else:
    print("result missmatch")

# close the browser.
browser.quit()
