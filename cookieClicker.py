from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options, service=Service(ChromeDriverManager().install()))

OPEN = True

driver.get("http://orteil.dashnet.org/experiments/cookie/")

cookie = driver.find_element(By.ID, "cookie")

items = driver.find_elements(By.CSS_SELECTOR, "#store div")
item_ids = [item.get_attribute("id") for item in items]

DOWNTIME = 1
timeout = time.time() + DOWNTIME

MAX_TIME = time.time() + 60*5.5

CURSOR_BUY = 60
MIN_TIME = time.time() + CURSOR_BUY


def buy_highest():
    global DOWNTIME
    down = DOWNTIME
    affordable = {}
    item_list = item_ids
    upgrades = {}

    prices = driver.find_elements(By.CSS_SELECTOR, "#store b")
    price_list = []
    for price in prices:
        text = price.text
        if text != "":
            price_list.append(int(text.split("-")[1].strip().replace(",", "")))

    for i in range(len(item_ids) - 1):
        upgrades[price_list[i]] = item_list[i]

    money = int(driver.find_element(By.ID, "money").text.replace(",", ""))

    for cost, name in upgrades.items():
        if money > cost:
            affordable[cost] = name

    try:
        highest = max(affordable)
    except ValueError:
        return

    can_buy = affordable[highest]
    # if time.time() > time.time() + CURSOR_BUY:
    #     DOWNTIME = 5
    #     print(down)
    #     if can_buy == "buyCursor":
    #         return

    buy = driver.find_element(By.ID, can_buy)
    buy.click()


while time.time() < MAX_TIME:
    if time.time() > timeout:
        if time.time() > MIN_TIME:
            DOWNTIME = 8
        buy_highest()
        timeout = time.time() + DOWNTIME
    cookie.click()

cookie_per_s = driver.find_element(By.ID, "cps").text
driver.quit()

with open("highscore.text", "a") as f:
    f.write(f"{cookie_per_s}: \n{MIN_TIME}\n{MAX_TIME}\n{CURSOR_BUY}\n")
print(cookie_per_s)