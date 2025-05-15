
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time


ser = Service(r"C:\drivers\chromedriver-win64\chromedriver.exe")
driver = webdriver.Chrome(service=ser)

driver.get("https://web.talenttitan.com/auth/login")

time.sleep(2)
print(driver.current_url)
print(driver.title)
driver.get("https://translate.google.co.in/?sl=auto&tl=te&op=translate")
time.sleep(2)

driver.back()
time.sleep(2)

driver.forward()





# driver.find_element(By.CSS_SELECTOR,"input#login-email-field").send_keys("dasarisaisumith@gmail.com")
# driver.find_element(By.NAME,"password").send_keys("Bondroy@123")
#
# s = driver.find_element(By.XPATH,"//a[@class='clickable']/parent::div")
# sr = driver.find_element(By.XPATH,"//a[@class='clickable']/ancestor::form")
#
# r = driver.find_element(By.XPATH,"//div[@fxlayoutalign='end center']/child::a")
# descendants_of_main = driver.find_elements(By.XPATH, "//div[@class='grecaptcha-logo']/descendant::*")
#
# for element in descendants_of_main:
#     print("Tag:", element.tag_name)
#
#
# print("parent node : ", s.get_attribute("fxlayoutalign"))
# print("ancestor node : ", sr.get_attribute("method"))
# print("child node : ", r.text)


#
# driver.find_element(By.XPATH, "//input[@type='submit']").click()
#
# driver.find_element(By.CSS_SELECTOR, "password").send_keys("Sumith@123")
#
# driver.find_element(By.XPATH, "//input[@type='submit']").click()






#driver.find_element(By.ID, "twotabsearchtextbox").send_keys("OnePlus Nord CE4 Lite 5G")

#driver.find_element(By.ID, "nav-search-submit-button").click()

# time.sleep(5)
#
# act_result = driver.title
# exp_result = "Amazon.in : log in"
#
# if act_result == exp_result:
#     print("login passed result")
# else :
#     print("login test failed")

#driver.close()
