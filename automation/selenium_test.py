from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time
import random
import string

# Setup driver automatically
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

# Open login page
driver.get("http://127.0.0.1:8000/login")

time.sleep(5)

# Random credentials
email = "user" + str(random.randint(1000, 9999)) + "@test.com"
password = ''.join(random.choices(string.ascii_letters + string.digits, k=8))

# Fill inputs
driver.find_element(By.NAME, "email_address").send_keys(email)
driver.find_element(By.NAME, "password").send_keys(password)

time.sleep(3)
driver.quit()
