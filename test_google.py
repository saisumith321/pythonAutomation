from selenium import webdriver

def test_google_title():
    driver = webdriver.Chrome(executable_path="chromedriver.exe")
    driver.get("https://www.google.com")
    assert "Google" in driver.title
    driver.quit()

if __name__ == "__main__":
    test_google_title()
