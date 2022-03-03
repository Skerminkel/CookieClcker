from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

driver.get("http://secure-retreat-92358.herokuapp.com/")

first_name = driver.find_element(By.NAME, "fName")
last_name = driver.find_element(By.NAME, "lName")
email = driver.find_element(By.NAME, "email")

first_name.send_keys("Wayne")
last_name.send_keys("Das")
email.send_keys("waynedas1@gmail.com")

button = driver.find_element(By.CSS_SELECTOR, "body form button")

button.click()
# driver.find_element(By.XPATH, "/html/body/form/button")
