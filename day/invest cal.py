import time
from selenium import webdriver
from selenium.webdriver.chrome.webdriver import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from day import Excelutils
import mysql.connector

s = Service(r"C:\Users\chromedriver-win64\chromedriver.exe")
driver = webdriver.Chrome(service=s)
driver.implicitly_wait(10)

driver.get("https://groww.in/calculators/sip-calculator")
driver.maximize_window()
#
# # print(input("sumith"))
#f2 = driver.find_element(By.XPATH,"//*[@id='root']/div[2]/div[1]/div[2]/div[1]/div[1]/div[2]/div[1]/div[4]/div[1]/div[2]/span/span")
# print(f2.text)
# file="C:\\Users\\harsh\\Documents\\sumith.xlsx"
# # sheet = "Sheet2"
# #
# # rows = Excelutils.Row(file,sheet)
# # print(rows)
# #
# # colum = Excelutils.Col(file,sheet)
# # print(colum)
try :
    con = mysql.connector.connect(host="localhost",port='3306',user="root",passwd="admin",database="schooldb")
    curs = con.cursor()
    curs.execute ("select * from Invest")

    for row in curs:

        am = row[0]
        du = row[1]
        ri = row[2]
        exp = row[3]

        f1 = driver.find_element(By.XPATH, "//*[@id='root']/div[2]/div[1]/div[2]/div[1]/div[1]/div[1]/div/div[2]/div[1]")
        driver.execute_script("arguments[0].scrollIntoView();", f1)

        driver.find_element(By.XPATH, "//input[@id='MONTHLY_INVESTMENT']").clear()
        driver.find_element(By.XPATH, "//input[@id='MONTHLY_INVESTMENT']").send_keys(am)
        time.sleep(3)

        driver.find_element(By.XPATH, "//input[@id='RETURN_RATE']").clear()
        driver.find_element(By.XPATH, "//input[@id='RETURN_RATE']").send_keys(du)

        driver.find_element(By.XPATH, "//input[@id='TIME_PERIOD']").clear()
        driver.find_element(By.XPATH, "//input[@id='TIME_PERIOD']").send_keys(ri)
        time.sleep(2)



        f2 = driver.find_element(By.XPATH,"//*[@id='root']/div[2]/div[1]/div[2]/div[1]/div[1]/div[2]/div[1]/div[4]/div[1]/div[2]/span/span").text
        # f3 = driver.find_element(By.XPATH,"//*[@id='root']/div[2]/div[1]/div[2]/div[1]/div[1]/div[2]/div[1]/div[4]/div[3]/div[2]/span/span").text


        if f2 == exp:
            print("test passed")
        else :
            print("Not test passed")
        time.sleep(3)
except:
    print("Something went wrong")

driver.close()
con.close()
    # Excelutils.write_data(file,"Sheet2",r,4,f2)
    # Excelutils.write_data(file,"Sheet2",r,5,f3)
    #
    # Excelutils.fill_green(file,"Sheet2",r,5)












