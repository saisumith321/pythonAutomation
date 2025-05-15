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

#save the screenshot in the current directory file
s = Service(r"C:\Users\chromedriver-win64\chromedriver.exe")
driver = webdriver.Chrome(service=s)
save = os.getcwd()


#save the screenshot in the other directory file
driver.get("https://www.amazon.in/stores/iQOO/page/291C27A4-502A-463E-A273-D2C362AF312A")
# driver.save_screenshot(save+"//PK1r.png")
cr = "C:\\Users\\harsh\\PycharmProjects\\python\\home.png"
driver.save_screenshot(cr)




# f1 = driver.find_element(By.XPATH,"//*[@id='Gutxbps8jq']/div/div/div/a")
# driver.execute_script("arguments[0].scrollIntoView(true);", f1)
# driver.save_screenshot(save+"//PK2r.png")
#
# time.sleep(3)
# driver.switch_to.new_window('tab')
#
# driver.get("https://www.cricbuzz.com/")
# driver.maximize_window()
#
# window_handles = driver.window_handles
#
# driver.switch_to.window(window_handles[0])
# time.sleep(4)
# cookies = driver.get_cookies()
# print("kcdkdmv",len(cookies))
#
# for cookie in cookies:
#     print(cookie.get("secure"))

