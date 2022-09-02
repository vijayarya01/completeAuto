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
xpath syntax or basic structure -- > //tag[@attribute="value"]
"""
#locating an element by relative xpath from webpage

#cart = driver.find_element(By.XPATH,'//a[@title="View my shopping cart"]').click()
#time.sleep(3)

# locating the element by absolute xpath from webpage
""" Well, we find the absolute path using the html tags from top of page till the length of our element which 
we want to locate. But, now a days, we have inbuilt extension to help you to find relative and absolute xpath.
"""
cart2 = driver.find_element(By.XPATH,'/html[1]/body[1]/div[1]/div[1]/header[1]/div[3]/div[1]/div[1]/div[3]/div[1]/a[1]').click()
time.sleep(3)
