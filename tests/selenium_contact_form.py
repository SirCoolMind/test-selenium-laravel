from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time

options = Options()
options.add_argument("--headless")
options.add_argument("--no-sandbox")

driver = webdriver.Chrome(options=options)

try:
    driver.get("http://localhost:8000/contact")
    time.sleep(2)

    # Select "Other" to trigger dynamic field
    topic = driver.find_element(By.ID, "topic")
    topic.find_element(By.XPATH, "//option[@value='other']").click()

    time.sleep(1)  # Wait for JS to show field

    # Fill out extra dynamic field
    driver.find_element(By.ID, "extra_field").send_keys("Custom Inquiry")

    # Message field
    driver.find_element(By.ID, "message").send_keys("Hello from Selenium!")

    # Submit
    driver.find_element(By.TAG_NAME, "button").click()
    time.sleep(1)

    # Check result
    body = driver.find_element(By.TAG_NAME, "body").text
    assert "Submitted: other - Hello from Selenium!" in body

    print("✅ Test passed!")

finally:
    driver.quit()