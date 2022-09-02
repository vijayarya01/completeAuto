import time
from selenium import webdriver
from selenium.webdriver.common.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

#initialize chrome driver manager
driver = webdriver.Chrome(ChromeDriverManager().install())


# Hit the url and open a webpage
driver.get("http://automationpractice.com/index.php")
driver.maximize_window()
time.sleep(2)

"""
Syntax and basic structure of the css_selector locator is : tag[attribue="value"] or 
in just case of div id in the webpage for css we can use this:   #value of id . as shown below in line of code.
in case of class , we can find css like this : a[class="value"] or .value of the tag.check line code 38 onwards
"""

#locating css element in the webpage.
#option 1
btnCart_css = driver.find_element(By.CSS_SELECTOR,'a[title="View my shopping cart"]').click() # Though we are
#assigning object to line of code but it does not return anything. We used it without in line 31
time.sleep(1)
print("The title cart page title is :", driver.title)
driver.minimize_window()
time.sleep(2)
#option 2
# imgLogo_css = driver.find_element(By.CSS_SELECTOR,'#header_logo').click()
# time.sleep(3)

# #option 3
driver.find_element(By.CSS_SELECTOR, 'div[id="header_logo"]').click()
time.sleep(1)
print("The title logo page title is:", driver.title)
driver.minimize_window()

time.sleep(2)
driver.maximize_window()

# using class attribute for css selector
driver.find_element(By.CSS_SELECTOR,'a[class="login"]').click()
#driver.find_element(By.CSS_SELECTOR,'.login').click
time.sleep(3)
print("The title of sign page is:" ,driver.title)
driver.minimize_window()
time.sleep(3)
driver.maximize_window()
driver.close()