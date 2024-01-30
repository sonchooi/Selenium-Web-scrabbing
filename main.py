from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from selenium import webdriver
import time

service = Service(executable_path="chromedriver.exe")
driver = webdriver.Chrome(service=service)

# Go to the site
driver.get("https://www.google.com/maps/")

# Fixing issues if there are some, Ex network lag, page loading, etc
WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.ID, "searchboxinput"))
)

# Select the portion that you want to work on
input_element = driver.find_element(By.ID, "searchboxinput")

# For input on that portion
input_element.send_keys("10 things to do in Canada" + Keys.ENTER)

# Wait for the elements to be present before scrolling
WebDriverWait(driver, 10).until(
    EC.presence_of_all_elements_located((By.CSS_SELECTOR, ".hfpxzc"))
)

for _ in range(3):  # Adjust the number of scrolls based on your needs
    # Select any element for which the 'send_keys' action is relevant
    driver.find_element(By.CSS_SELECTOR, '.hfpxzc').send_keys(Keys.END)
    time.sleep(2)

try:
    # Locate all anchor elements by CSS selector
    WebDriverWait(driver, 10).until(
        EC.presence_of_all_elements_located((By.CSS_SELECTOR, ".hfpxzc"))
    )

    anchor_elements = driver.find_elements(By.CSS_SELECTOR, ".hfpxzc")

    # Check if there's at least one element in the list
    if anchor_elements:
        for i in range(0, 10):
            aria_label = anchor_elements[i].get_attribute("aria-label")
            print(aria_label)
    else:
        print("No elements found with the specified CSS selector.")

except Exception as e:
    print(f"Error: {e}")

finally:
    # Close the webdriver
    time.sleep(10)
    driver.quit()
