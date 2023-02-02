import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager


class TestLogin(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Chrome(ChromeDriverManager().install())

    def test_01_success_login(self):
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
        # validasi
        expectedURL = "https://www.saucedemo.com/inventory.html"
        actualURL = browser.current_url
        self.assertEquals(expectedURL, actualURL)

    def test_02_failed_login_invalid_username(self):
        # steps
        browser = self.browser  # buka web browser
        browser.get("https://www.saucedemo.com/")  # buka situs
        # layar penuh page
        browser.maximize_window()
        time.sleep(3)
        browser.find_element(
            By.ID, "user-name").send_keys("jawa")  # isi email
        time.sleep(1)
        browser.find_element(By.ID, "password").send_keys(
            "secret_sauce")  # isi password
        time.sleep(1)
        # klik tombol sign in
        browser.find_element(By.ID, "login-button").click()
        time.sleep(1)
        # validasi
        response_message = browser.find_element(
            By.XPATH, "/html/body/div/div/div[2]/div[1]/div[1]/div/form/div[3]/h3").text
        self.assertEqual(
            response_message, 'Epic sadface: Username and password do not match any user in this service')

    def test_03_failed_login_invalid_password(self):
        # steps
        # buka web browser
        browser = self.browser
        # buka situs
        browser.get("https://www.saucedemo.com/")
        # layar penuh page
        browser.maximize_window()
        time.sleep(3)
        # isi username
        browser.find_element(
            By.ID, "user-name").send_keys("standard_user")
        time.sleep(1)
        # isi password
        browser.find_element(By.ID, "password").send_keys(
            "12345678910")
        time.sleep(1)
        # klik tombol sign in
        browser.find_element(By.ID, "login-button").click()
        time.sleep(1)
        # validasi
        response_message = browser.find_element(
            By.XPATH, "/html/body/div/div/div[2]/div[1]/div[1]/div/form/div[3]/h3").text
        self.assertEqual(
            response_message, 'Epic sadface: Username and password do not match any user in this service')

    def test_04_failed_login_invalid_username_password(self):
        # steps
        # buka web browser
        browser = self.browser
        # buka situs
        browser.get("https://www.saucedemo.com/")
        # layar penuh page
        browser.maximize_window()
        time.sleep(3)
        # isi username
        browser.find_element(By.ID, "user-name").send_keys("jawa")
        time.sleep(1)
        # isi password
        browser.find_element(By.ID, "password").send_keys("only")
        time.sleep(1)
        # klik tombol sign in
        browser.find_element(By.ID, "login-button").click()
        time.sleep(1)
        # validasi
        response_message = browser.find_element(
            By.XPATH, "/html/body/div/div/div[2]/div[1]/div[1]/div/form/div[3]/h3").text
        self.assertEqual(
            response_message, 'Epic sadface: Username and password do not match any user in this service')

    def test_05_failed_login_blank_field(self):
        # steps
        # buka web browser
        browser = self.browser
        # buka situs
        browser.get("https://www.saucedemo.com/")
        # layar penuh page
        browser.maximize_window()
        time.sleep(3)
        # isi username
        browser.find_element(By.ID, "user-name").send_keys("")
        time.sleep(1)
        # isi password
        browser.find_element(By.ID, "password").send_keys("")
        time.sleep(1)
        # klik tombol sign in
        browser.find_element(By.ID, "login-button").click()
        time.sleep(1)
        # validasi
        response_message = browser.find_element(
            By.XPATH, "/html/body/div/div/div[2]/div[1]/div[1]/div/form/div[3]/h3").text
        self.assertEqual(response_message,
                         'Epic sadface: Username is required')

    def tearDown(self):
        self.browser.close()


if __name__ == "__main__":
    unittest.main()
