import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager


class TestAbout(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Chrome(ChromeDriverManager().install())

    def test_about(self):
        # steps
        # buka web browser
        browser = self.browser
        # buka situs
        browser.get("https://www.saucedemo.com/")
        # layar penuh page
        browser.maximize_window()
        time.sleep(3)
        # isi username
        browser.find_element(By.ID, "user-name").send_keys("standard_user")
        time.sleep(1)
        # isi password
        browser.find_element(By.ID, "password").send_keys("secret_sauce")
        time.sleep(1)
        # klik tombol sign in
        browser.find_element(By.ID, "login-button").click()
        time.sleep(1)
        # click toggle menu
        browser.find_element(By.ID, "react-burger-menu-btn").click()
        time.sleep(1)
        # klik menu about
        browser.find_element(By.ID, "about_sidebar_link").click()
        time.sleep(1)
        # validasi
        expectedURL = "https://saucelabs.com/"
        actualURL = browser.current_url
        self.assertEquals(expectedURL, actualURL)

    def tearDown(self):
        self.browser.close()


if __name__ == "__main__":
    unittest.main()
