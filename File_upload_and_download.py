import time

from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.devtools.v134.css import CSSLayer
from selenium.webdriver.support.ui import Select
from selenium import webdriver
from selenium.webdriver import ActionChains

from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os
location = os.getcwd()

# DOWNLOAD THE FILE
# def Chrome():
#     from selenium.webdriver.chrome.service import Service
#     ser = Service(r"C:\Users\chromedriver-win64\chromedriver.exe")
#
#     preferences = {"download.default_directory": location}
#     ops= webdriver.ChromeOptions()
#     ops.add_experimental_option("prefs", preferences)
#
#     driver = webdriver.Chrome(service=ser, options=ops)
#     return driver
#
# obj = Chrome()
# obj.get("https://sample-files.com/documents/txt/")
# obj.maximize_window()
# file = obj.find_element(By.XPATH,"//a[text()='Download Simple Text']")
# obj.execute_script("arguments[0].scrollIntoView();", file)
# print(input("jf vfv "))
# time.sleep(5)
# file.click()
# time.sleep(2)

#UPLOAD THE FILES

s = Service(r"C:\Users\chromedriver-win64\chromedriver.exe")
driver = webdriver.Chrome(service=s)
wait = WebDriverWait(driver, 10)

driver.get("https://practice.expandtesting.com/upload")
time.sleep(4)
driver.maximize_window()
f1 = driver.find_element(By.XPATH,"//input[@type='file']")
driver.execute_script("arguments[0].scrollIntoView(true);", f1)
f1.send_keys("C:\Intel\sum.pdf")

time.sleep(5)


