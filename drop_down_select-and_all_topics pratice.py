import select
import time
from selenium.webdriver import ActionChains
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

S = Service(r"C:\Users\chromedriver-win64\chromedriver.exe")
driver = webdriver.Chrome(service=S)

driver.get("https://testautomationpractice.blogspot.com/")
driver.maximize_window()


#USING SELECT AND OPTION  METHOD
#dropdown = driver.find_element(By.ID,"country")
#Select = Select(dropdown)
#Select.select_by_visible_text("India")

#for options in Select.options:
 #   print(options.text)

#direct select with for loop
# Menu = driver.find_elements(By.XPATH,'//*[@id="country"]/option')
#
# for option in Menu:
#     a = option.text
#     if a == "Brazil":
#         option.click()
#
# time.sleep(5)


#date picker

# driver.find_element(By.CLASS_NAME,"hasDatepicker").click()
#
#
# month = "December"
# year = "2025"
# date = "13"
#
# while True:
#     mon = driver.find_element(By.XPATH,"//span[@class='ui-datepicker-month']").text
#     ye = driver.find_element(By.XPATH,"//span[@class='ui-datepicker-year']").text
#
#
#     if month == mon and year == ye:
#         dat = driver.find_elements(By.XPATH, "//*[@id='ui-datepicker-div']/table/tbody/tr/td/a")
#         for ele in dat:
#             if ele.text == date:
#                 ele.click()
#                 time.sleep(5)
#                 break
#     else :
#         driver.find_element(By.XPATH,"//span[@class='ui-icon ui-icon-circle-triangle-e']").click()


# click the chekbox

# click = driver.find_elements(By.XPATH,"//*[@id='post-body-1307673142697428135']/div[4]/div/label")
# l = []
# for i in click:
#     l.append(i.text)
# print(l)
# print(len(l))

#alters

# driver.find_element(By.ID,"alertBtn").click()
# time.sleep(5)
# alert = driver.switch_to.alert
# alert.accept()
#
# driver.find_element(By.ID, "confirmBtn").click()
# time.sleep(4)
# alert = driver.switch_to.alert
# alert.accept()
#
# driver.find_element(By.ID, "promptBtn").click()
# time.sleep(4)
# alert = driver.switch_to.alert
# alert.send_keys("sai sumith")

#GO BACK TO FIRST WINDOW AND CLICK GO TO FORWARD WINDOW
# driver.find_element(By.LINK_TEXT,"Blog").click()
# driver.back()
# time.sleep(3)
# driver.forward()
# time.sleep(3)

# driver.find_element(By.XPATH,"//button[text()='New Tab']").click()
# time.sleep(3)
# windows =  driver.window_handles
#
#
# driver.switch_to.window(windows[0])
# time.sleep(3)
# print("Switched back to main tab:", driver.title)

#drag_and drop

source = driver.find_element(By.XPATH, "//*[@id='draggable']")
target = driver.find_element(By.XPATH, "//*[@id='droppable']")

actions = ActionChains(driver)
actions.drag_and_drop(source, target).perform()

ele = driver.find_element(By.XPATH,"//*[@id='post-body-1307673142697428135']/div[8]/button")

actions = ActionChains(driver)
actions.move_to_element(ele).perform()
time.sleep(5)













