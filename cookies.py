import time
from selenium import webdriver
from selenium.webdriver.chrome.webdriver import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

s = Service(r"C:\Users\chromedriver-win64\chromedriver.exe")
driver = webdriver.Chrome(service=s)

driver.get("https://openai.com/index/chatgpt/")
p = driver.get_cookies()
print(p)


# #adding the cookie to the browser
# driver.add_cookie({"name" : "buv","value" : "fbd"})
# p = driver.get_cookies()
# print(len(p))
#
# #deleting the specific cookie from browser
# driver.delete_cookie({"buv"})
# p = driver.get_cookies()
# print(len(p))
#
# #delete all the cookies
# driver.delete_all_cookies()
# p = driver.get_cookies()
# print(len(p))

# for cookie in p:
#     print(cookie)



