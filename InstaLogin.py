from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

class InstaLogin:

    logged_in = False

    def __init__(self, username, password, chrome_driver_path):
        self.username = username
        self.password = password
        self.driver = webdriver.Chrome(chrome_driver_path)
        self.login()

    def login(self):
        if not InstaLogin.logged_in:
            InstaLogin.logged_in = True
            self.driver.get("https://instagram.com")
            time.sleep(3)
            username = self.driver.find_element_by_name('username')
            username.send_keys(self.username)
            password = self.driver.find_element_by_name('password')
            password.send_keys(self.password)
            self.driver.find_element_by_xpath('//*[@id="loginForm"]/div/div[3]/button').click()
            time.sleep(3)
            self.driver.find_element_by_xpath("//button[contains(text(), 'Not Now')]").click()
            time.sleep(2)
            self.driver.find_element_by_xpath("//button[contains(text(), 'Not Now')]").click()
            time.sleep(2)

    def goToProfilePage(self):
        self.driver.get("https://www.instagram.com/" + self.username + "/")
        time.sleep(3)

    def goToMainFeedPage(self):
        self.driver.get("https://www.instagram.com/")
        time.sleep(3)

    def goToExplorePage(self):
        self.driver.get("https://www.instagram.com/explore/")
        time.sleep(3)