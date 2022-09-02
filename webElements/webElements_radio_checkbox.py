from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.service import Service
from selenium.webdriver.support import wait
from selenium.webdriver.support.select import Select
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time

#initialize chrome driver manager
driver = webdriver.Chrome(ChromeDriverManager().install())
fashion_url = "http://automationpractice.com/index.php"
travel_url = "https://www.edreams.com/"

# Hit the url and open a webpage
driver.get(travel_url)
driver.maximize_window()
time.sleep(2)
print("Welcome to first page, ", driver.title)
'''
txt_searchBox_id = driver.find_element(By.ID,'search_query_top')
txt_searchBox_id.click()
txt_searchBox_id.send_keys("dressess")
txt_searchBox_id.send_keys(Keys.BACKSPACE)
time.sleep(3)
btn_Submit_name = driver.find_element(By.NAME,'submit_search').click()

time.sleep(5)

'''
'''
We need to handle such pop up which comes generally only once, if we hard code it like below, it will fail here.
We need to code such that if it appears, handle it else move to next step.

#line of code
driver.find_element(By.ID,'didomi-notice-agree-button').click()
time.sleep(5)
'''
'''
Requirements: Flight from Paris(Airport: Orly) to Berlin (Airport: Schoenefeld)
Departure date : 21.12.2022 
Return date : 04.03.2023

'''

# We need to handle such pop up which comes generally only once, if we hard code it like below, it will fail here.
# We need to code such that if it appears, handle it else move to next step.
driver.find_element(By.ID,'didomi-notice-agree-button').click()
time.sleep(5)
# Radio buttons
rb_oneway_xpath = driver.find_element(By.XPATH,"//span[contains(text(),'One way')]")
rb_oneway_xpath.click()

#Check box
cb_directFlights_xpath = driver.find_element(By.XPATH,"//div[contains(text(),'Direct flights only')]")
cb_directFlights_xpath.click()
time.sleep(1)

tab_hotel_xpath = driver.find_element(By.XPATH,'//span[contains(text(),"Hotels")]').click()
time.sleep(5)

# Below line of code is in frames, so we need need to handle frames with this code immediately below

#Work with frames-- > This can be done by index, id or name
iframe = driver.find_element(By.CSS_SELECTOR,"iframe.iframe_manager")

driver.switch_to.frame(iframe)
driver.implicitly_wait(10)
#Work with static Drop down values, it can be handle by three ways.
# Select 2 rooms

dd_rooms_name = driver.find_element(By.CSS_SELECTOR,"select.aff-groupselection__element[aria-label='Number of rooms']")
dropdown_1 = Select(dd_rooms_name)
dropdown_1.select_by_index('1') # it has a value of 2 at index 1.
time.sleep(1)
# Select 3 adults
dd_adults_name = driver.find_element(By.CSS_SELECTOR,'select.aff-groupselection__element[name="group_adults"]')
dropdown_2 = Select(dd_adults_name).select_by_value('3')
time.sleep(2)
#Select 4 children
dd_child_name = driver.find_element(By.CSS_SELECTOR,'select.aff-groupselection__element[name="group_children"]')
dropdown_3 = Select(dd_child_name).select_by_visible_text('4')
time.sleep(3)

# switch to default content
driver.switch_to.default_content()
time.sleep(2)

# Back to Select Flights sections after exiting from iframe as written above lines of code
flights_xpath = driver.find_element(By.XPATH,"//div/span[2][text()='Flights']").click()
time.sleep(5)

# From where selecting airport
departure_city_css = driver.find_element(By.CSS_SELECTOR,'input[placeholder="Where from?"]').send_keys("Paris")
#departure_city_css.send_keys("Paris")

item_airports = driver.find_element(By.XPATH, "//span[contains(text(),'Orly')]").click()

arrival_city_css = driver.find_element(By.CSS_SELECTOR,'input[placeholder="Where to?"]').send_keys("Berlin")




