from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium import common
import time

TWITTER_EMAIL = "*****"
TWITTER_PASSWORD = "***"
CHROME_DRIVER_PATH = "D:\chromedriver\chromedriver.exe"


class InternetSpeedTwitterBot:
    def __init__(self, driver_path):
        service = Service(driver_path)
        self.driver = webdriver.Chrome(service=service)
        self.up = 0
        self.down = 0

    def get_internet_speed(self):
        self.driver.get("https://www.speedtest.net/")
        self.driver.find_element(By.ID, "_evidon-banner-acceptbutton").click()
        time.sleep(3)
        self.driver.find_element(By.CLASS_NAME, "start-text").click()
        time.sleep(50)
        self.driver.find_element(By.XPATH,
                                 "/html/body/div[3]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[8]/div/div/div[2]/a").click()
        self.down = self.driver.find_element(By.CLASS_NAME, "download-speed").text
        self.up = self.driver.find_element(By.CLASS_NAME, "upload-speed").text

    def login_twitter(self):
        self.driver.get("https://twitter.com/i/flow/login")
        time.sleep(3)
        email_container = self.driver.find_element(By.NAME, 'text')
        email_container.send_keys(TWITTER_EMAIL)
        email_container.send_keys(Keys.ENTER)
        time.sleep(2)
        try:
            email_container = self.driver.find_element(By.NAME, 'text')
            email_container.send_keys('@NetSpeedBot')
            email_container.send_keys(Keys.ENTER)
        except common.exceptions.NoSuchElementException:
            pass
        time.sleep(2)
        password_container = self.driver.find_element(By.NAME, "password")
        password_container.send_keys(TWITTER_PASSWORD)
        password_container.send_keys(Keys.ENTER)

    def tweet_at_provider(self):
        self.login_twitter()
        time.sleep(4)
        text_box = self.driver.find_element(By.CLASS_NAME, "public-DraftEditor-content")
        text_box.send_keys(f"My internet speed now is {self.down} down/ {self.up} up. ")
        self.driver.find_element(By.XPATH,"/html/body/div[1]/div/div/div[2]/main/div/div/div/div/div/div[2]/div/div[2]/div[1]/div/div/div/div[2]/div[3]/div/div/div[2]/div[3]").click()


bot = InternetSpeedTwitterBot(CHROME_DRIVER_PATH)
bot.get_internet_speed()
bot.tweet_at_provider()
