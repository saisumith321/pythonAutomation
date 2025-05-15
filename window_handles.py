import time
from selenium.webdriver.support.ui import Select
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.webdriver import Service, WebDriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os

s = Service(r"C:\Users\chromedriver-win64\chromedriver.exe")
driver = webdriver.Chrome(service=s)

driver.get("https://www.cricbuzz.com/")

driver.switch_to.new_window('tab')
print("openeing the second page")


driver.get("https://www.infosys.com/")
driver.maximize_window()
time.sleep(3)
driver.find_element(By.CSS_SELECTOR,"a[title='Explore Careers Opportunities']").click()
time.sleep(3)
driver.back()


f1 = driver.window_handles

driver.switch_to.window(f1[0])

time.sleep(3)