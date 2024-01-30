from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

service =  Service(executable_path="chromedriver.exe")
driver = webdriver.Chrome(service=service)


#go to the site
driver.get("https://google.com")

#Fixing issues if there are some, Ex network lag, page loading etc
WebDriverWait(driver, 5).until(
    EC.presence_of_all_elements_located((By.CLASS_NAME,"gLFyf"))
)


#select the portion that you want to work on
input_element = driver.find_element(By.CLASS_NAME,"gLFyf")

#for input on that portion
input_element.clear()
input_element.send_keys("skyranko" + Keys.ENTER)





time.sleep(10)
driver.quit()
