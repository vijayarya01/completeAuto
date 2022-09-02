import time
from selenium import webdriver
from selenium.webdriver.common.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options

#We can alos initialize the browser headless using below line of code
chrome_options = Options()
chrome_options.add_argument('--headless')


#initialize chrome driver manager
driver = webdriver.Chrome(ChromeDriverManager().install(),options=chrome_options)


#serv_obj = Service("/Users/vijaydudhiyan/webdrivers/chromedriver.exe")
#driver = webdriver.Chrome(executable_path="/Users/vijaydudhiyan/webdrivers/chromedriver.exe")
# Hit the url and open a webpage
driver.get("http://automationpractice.com/index.php")
driver.maximize_window()

#Contact us button
driver.find_element(By.XPATH,'//header/div[2]/div[1]/div[1]/nav[1]/div[2]/a[1]').click()
time.sleep(2)

#Go Back button
driver.back()
time.sleep(2)

#Go-forward
driver.forward()
time.sleep(2)

#print the title
contact_title = driver.title
time.sleep(2)
print("The title of this current page is: ", contact_title)

#minimize the windoe
driver.minimize_window()
time.sleep(2)
#maximize the window
driver.maximize_window()
time.sleep(2)

#printCurrentURL
current_url = driver.current_url
print("The current url is :", current_url)

#Refresht or reload the page
driver.refresh()

driver.close()
print("The browser closed successfully.Mate..Cheers")
