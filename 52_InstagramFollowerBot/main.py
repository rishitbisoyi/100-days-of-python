from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

SIMILAR_ACCOUNT = "FOLLOWERS_ACCOUNT"
USERNAME = "INSTAGRAM_USERNAME"
PASSWORD = "INSTAGRAM_PASSWORD"


class InstaFollower:

    def __init__(self):
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_experimental_option("detach", True)
        self.driver = webdriver.Chrome(options=chrome_options)

    def login(self):
        self.driver.get("https://www.instagram.com/accounts/login/")
        time.sleep(5)

        cookie_buttons = self.driver.find_elements(
            By.XPATH,
            "//button[contains(text(), 'Decline') or contains(text(), 'Allow essential')]"
        )

        if cookie_buttons:
            cookie_buttons[0].click()

        username = self.driver.find_element(By.NAME, "username")
        password = self.driver.find_element(By.NAME, "password")

        username.send_keys(USERNAME)
        password.send_keys(PASSWORD)
        password.send_keys(Keys.ENTER)

        time.sleep(6)

        not_now_buttons = self.driver.find_elements(
            By.XPATH,
            "//button[contains(text(), 'Not now')]"
        )

        if not_now_buttons:
            not_now_buttons[0].click()

        time.sleep(3)

        not_now_buttons = self.driver.find_elements(
            By.XPATH,
            "//button[contains(text(), 'Not Now')]"
        )

        if not_now_buttons:
            not_now_buttons[0].click()

    def find_followers(self):
        time.sleep(3)

        self.driver.get(f"https://www.instagram.com/{SIMILAR_ACCOUNT}/followers")
        time.sleep(5)

        dialog = self.driver.find_element(
            By.XPATH,
            "//div[@role='dialog']"
        )

        for _ in range(10):
            self.driver.execute_script(
                "arguments[0].scrollTop = arguments[0].scrollHeight",
                dialog
            )
            time.sleep(2)

    def follow(self):
        buttons = self.driver.find_elements(
            By.XPATH,
            "//div[@role='dialog']//button[contains(text(), 'Follow')]"
        )

        for button in buttons:
            try:
                button.click()
                time.sleep(1)
            except:
                pass


bot = InstaFollower()
bot.login()
bot.find_followers()
bot.follow()