from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

driver.get("http://python.org")

data = driver.find_elements(By.CSS_SELECTOR, '.event-widget .shrubbery .menu li')


data_dict = {
    i: {"time": j.find_element(By.TAG_NAME, "time").text,
        "date": j.find_element(By.TAG_NAME, "a").text} for i, j in enumerate(data)
}

print(data_dict)

