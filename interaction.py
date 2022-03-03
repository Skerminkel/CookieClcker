from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

# chrome_options = Options()
# chrome_options.add_experimental_option("detach", True)
# chrome_options.AddExcludedArgument("enable-automation")

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

driver.get("https://en.wikipedia.org/wiki/Main_Page")

# data = driver.find_element(By.ID, "articlecount").find_element(By.CSS_SELECTOR, "a")

search = driver.find_element(By.NAME, "search")
search.send_keys("Python", Keys.ENTER)
# search.send_keys(Keys.ENTER)


# all_portals = driver.find_element(By.LINK_TEXT, "All portals")
# all_portals.click()

# print(data)
