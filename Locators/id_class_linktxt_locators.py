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

# Locating an element using ID
searchbar_id = driver.find_element(By.ID,'search_query_top').send_keys("hello")


#Locating an element using Name
btnSubmit_class = driver.find_element(By.NAME,'submit_search').submit()
print("The title of this search page is ",driver.title)
time.sleep(5)

#locating an element using Class_Name
signIn_class = driver.find_element(By.CLASS_NAME,'login').click()
print("The title of this page is," ,driver.title)


# locating an element using Link_text
contactUs_linkTxt = driver.find_element(By.LINK_TEXT,'Contact us').click()
print("The title of page is ",driver.title)
time.sleep(5)
driver.minimize_window()
time.sleep(3)
# locating an element using Partial_Link_Text --> just pass partial keyword from text itself.

#contactUs_linkTxt = driver.find_element(By.PARTIAL_LINK_TEXT,'Contac').click()

driver.maximize_window()
time.sleep(2)
driver.close()