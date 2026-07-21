from selenium import webdriver
from selenium.webdriver.common.by import By
import time

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)

driver.get("https://orteil.dashnet.org/experiments/cookie/")

cookie = driver.find_element(By.ID, "cookie")

timeout = time.time() + 5
five_minutes = time.time() + 60 * 5

while True:
    cookie.click()

    if time.time() > timeout:

        money = int(driver.find_element(By.ID, "money").text.replace(",", ""))

        store = driver.find_elements(By.CSS_SELECTOR, "#store div")

        affordable = []

        for item in store:
            if "grayed" not in item.get_attribute("class"):
                affordable.append(item)

        if affordable:
            affordable[-1].click()

        timeout = time.time() + 5

    if time.time() > five_minutes:
        cookies_per_sec = driver.find_element(By.ID, "cps").text
        print(cookies_per_sec)
        break

driver.quit()