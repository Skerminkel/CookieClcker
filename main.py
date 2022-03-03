from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

driver.get("https://www.amazon.com/EVGA-06G-P4-2068-KR-GeForce-Gaming-Backplate/dp/B083GGYNQ6/?_encoding=UTF8&pd_rd_w=i22g9&pf_rd_p=6f8f01b9-e98c-4b0d-91cf-a93790267134&pf_rd_r=1P5633YNHX655HERCMVX&pd_rd_r=3c070e36-89c4-4e20-80cd-9e617a2f611d&pd_rd_wg=1VC4P&ref_=pd_gw_ci_mcx_mr_hp_atf_m")

price = driver.find_element(By.ID, "price_inside_buybox")

# driver.find_element(By.XPATH, '//*[@id="site-map"]/div[2]/div/ul/li[4]/a')
# driver.find_elements(By.CSS_SELECTOR, '.event-widget time')
# driver.find_elements(By.CSS_SELECTOR, '.event-widget li a')

# driver.close()  # closes one tab
# driver.quit()  # closes everything

# random = driver.find_element(By.XPATH, '//*[@id="productSupportAndReturnPolicy-product-support-policy-anchor-text"]')

print(random.get_dom_attribute('href'))