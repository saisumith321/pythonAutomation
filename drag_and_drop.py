import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.webdriver import Service, WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

s = Service(r"C:\Users\chromedriver-win64\chromedriver.exe")
driver = webdriver.Chrome(service=s)
wait = WebDriverWait(driver, 5)

driver.get('https://demo.automationtesting.in/Static.html')
driver.maximize_window()


f1 = driver.find_element(By.XPATH,"/html[1]/body[1]/section[1]/div[1]/div[1]/div[1]/div[1]/img[1]")
driver.execute_script("arguments[0].scrollIntoView();", f1)
f2 = driver.find_element(By.XPATH,"/html[1]/body[1]/section[1]/div[1]/div[1]/div[2]/div[1]")

actions = ActionChains(driver)

actions.drag_and_drop(f1, f2).perform()

time.sleep(5)







