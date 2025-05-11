import time

from selenium import webdriver
from selenium.webdriver.chrome.webdriver import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


service = Service(r"C:\drivers\chromedriver-win64\chromedriver.exe")
drive = webdriver.Chrome(service=service)

# drive.get("https://opensource-demo.orangehrmlive.com/web/index.php/admin/viewSystemUsers")
drive.get("https://afd.calpoly.edu/web/sample-tables")
time.sleep(2)

# drive.find_element(By.NAME,"username").send_keys("Admin")
# time.sleep(2)
# drive.find_element(By.NAME,"password").send_keys("admin123")
# time.sleep(2)
# drive.find_element(By.XPATH,"//*[@id='app']/div[1]/div/div[1]/div/div[2]/div[2]/form/div[3]/button").click()
#
# time.sleep(2)
#orange hrm

# drive.find_element(By.XPATH,"//*[@id='app']/div[1]/div[1]/aside/nav/div[2]/ul/li[1]/a").click()
# td = drive.find_elements(By.XPATH,"//*[@id='app']/div[1]/div[2]/div[2]/div/div[2]/div[3]/div/div[1]/div/div")
#
#
# for i in td:
#     tf = i.get_attribute("class")
#     print(tf)




# Get all rows
t0 = drive.find_elements(By.XPATH, "//*[@id='content']/table[1]/tbody/tr[1]/th")

print("no of rows:", len(t0))  # Example: 7

for i in range(3):
    s = t0[i].text
    print(s)


# # Get all columns from the first row
# t1 = drive.find_elements(By.XPATH, "//*[@id='content']/table[1]/tbody/tr[1]/th")
# print("no of columns:", len(t1))  # Example: 3
#
# ex = []
# for i in range(2, len(t0)+1 ):
#     # for j in range(1, len(t1)):  # XPath is 1-based
#     data =  drive.find_element(By.XPATH, "//*[@id='content']/table[1]/tbody/tr["+str(i)+"]/td[2]").text
#     ex.append(data)
#
# print(ex)








# t2 = drive.find_elements(By.XPATH,"//*[@id='pointtable']/div/div/div[1]/div/div/div[2]/div/div/div/table//tr//th")
#
#
# g = []
#
# for i in range(len(t2)):
#     h = t2[i].text
#     g.append(h)
# print(g)
#
# t3 = drive.find_elements(By.XPATH,"//*[@id='pointsdata']/tr[1]/td")
# print(len(t3))
#
# g1 = []
# for j in range(len(t3)):
#     h1 = t3[j].text
#     g1.append(h1)
# print(g1)






