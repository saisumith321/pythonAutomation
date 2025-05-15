from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import time

# Setup ChromeDriver path
s = Service(r"C:\Users\chromedriver-win64\chromedriver.exe")
driver = webdriver.Chrome(service=s)

# Open a webpage with an iframe
driver.get("https://demo.automationtesting.in/Frames.html")

# Maximize window and wait
driver.maximize_window()
time.sleep(3)

# Switch to the first iframe on the page

driver.find_element(By.XPATH,"//a[text()='Iframe with in an Iframe']").click()

driver.switch_to.frame(driver.find_element(By.XPATH,"//*[@id='Multiple']/iframe"))
driver.switch_to.frame(driver.find_element(By.CSS_SELECTOR,"iframe[src='SingleFrame.html']"))


# Now switch to the inner iframe inside the outer iframe
driver.find_element(By.XPATH,"//input[@type='text']").send_keys("msnkccnkcndc")
time.sleep(5)