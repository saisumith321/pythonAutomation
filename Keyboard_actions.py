import time
from selenium.webdriver.support.ui import Select
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.webdriver import Service, WebDriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

s = Service(r"C:\Users\chromedriver-win64\chromedriver.exe")
driver = webdriver.Chrome(service=s)

#COPY AND PASTE USING MOUSE ACTIONS
driver.get("https://testautomationpractice.blogspot.com/")
driver.maximize_window()
element = driver.find_element(By.XPATH,"//*[@id='name']")
driver.execute_script("arguments[0].scrollIntoView(true);", element)


first = driver.find_element(By.XPATH,"//*[@id='name']")
second = driver.find_element(By.XPATH,"//*[@id='email']")

first.send_keys("ersdfghjkl;")

action = ActionChains(driver)

action.key_down(Keys.CONTROL).send_keys("a").key_up(Keys.CONTROL).perform()
action.key_down(Keys.CONTROL).send_keys("c").key_up(Keys.CONTROL).perform()
action.send_keys(Keys.TAB).perform()
action.key_down(Keys.CONTROL).send_keys("v").key_up(Keys.CONTROL).perform()

time.sleep(3)


check = driver.find_elements(By.XPATH,"//input[@class='form-check-input' and @type='checkbox']")

for i in range(len(check)):
    g = check[i].get_attribute("value")
    if g == "monday" or  g == "tuesday"  :
        check[i].click()


time.sleep(5)



# #SELECT THE ITEMS IN THE DROPDOWN SECTION
# le = Select(driver.find_element(By.XPATH,"//*[@id='country']"))
#
# se = le.options
#
# for i in range(len(se)):3
#     g = se[i].text
#     if g == "France":
#         se[i].click()











