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

    def test_01_succces_login(self):
        browser = self.browser
        browser.get("https://opensource-demo.orangehrmlive.com/")  # buka situs
        browser.maximize_window()
        time.sleep(5)
        # isi username
        browser.find_element(
            By.XPATH, "/html/body/div/div[1]/div/div[1]/div/div[2]/div[2]/form/div[1]/div/div[2]/input").send_keys("Admin")
        time.sleep(1)
        # isi password
        browser.find_element(
            By.XPATH, "//*[@id='app']/div[1]/div/div[1]/div/div[2]/div[2]/form/div[2]/div/div[2]/input").send_keys("admin123")
        time.sleep(1)
        # klik buton login
        browser.find_element(
            By.XPATH, "/html/body/div/div[1]/div/div[1]/div/div[2]/div[2]/form/div[3]/button").click()
        time.sleep(8)
        # validasi
        expectedURL = "https://opensource-demo.orangehrmlive.com/web/index.php/dashboard/index"
        actualURL = browser.current_url
        self.assertEquals(expectedURL, actualURL)

    def test_02_failed_login_with_invalid_username(self):
        browser = self.browser
        browser.get("https://opensource-demo.orangehrmlive.com/")  # buka situs
        browser.maximize_window()
        time.sleep(5)
        # isi username
        browser.find_element(
            By.XPATH, "/html/body/div/div[1]/div/div[1]/div/div[2]/div[2]/form/div[1]/div/div[2]/input").send_keys("Yantobasna")
        time.sleep(1)
        # isi password
        browser.find_element(
            By.XPATH, "//*[@id='app']/div[1]/div/div[1]/div/div[2]/div[2]/form/div[2]/div/div[2]/input").send_keys("admin123")
        time.sleep(1)
        # klik buton login
        browser.find_element(
            By.XPATH, "/html/body/div/div[1]/div/div[1]/div/div[2]/div[2]/form/div[3]/button").click()
        time.sleep(5)
        # validasi
        response_message = browser.find_element(
            By.XPATH, "/html/body/div/div[1]/div/div[1]/div/div[2]/div[2]/div/div[1]/div[1]/p").text
        self.assertIn(response_message, 'Invalid credentials')

    def test_03_failed_login_with_invalid_password(self):
        browser = self.browser
        browser.get("https://opensource-demo.orangehrmlive.com/")  # buka situs
        browser.maximize_window()
        time.sleep(5)
        # isi username
        browser.find_element(
            By.XPATH, "/html/body/div/div[1]/div/div[1]/div/div[2]/div[2]/form/div[1]/div/div[2]/input").send_keys("Admin")
        time.sleep(1)
        # isi password
        browser.find_element(
            By.XPATH, "//*[@id='app']/div[1]/div/div[1]/div/div[2]/div[2]/form/div[2]/div/div[2]/input").send_keys("yanto123")
        time.sleep(1)
        # klik buton login
        browser.find_element(
            By.XPATH, "/html/body/div/div[1]/div/div[1]/div/div[2]/div[2]/form/div[3]/button").click()
        time.sleep(5)
        # validasi
        response_message = browser.find_element(
            By.XPATH, "/html/body/div/div[1]/div/div[1]/div/div[2]/div[2]/div/div[1]/div[1]/p").text
        self.assertIn(response_message, 'Invalid credentials')

    def test_04_failed_login_with_invalid_username_password(self):
        # buka browser
        browser = self.browser
        # buka situs
        browser.get("https://opensource-demo.orangehrmlive.com/")
        # maximize window
        browser.maximize_window()
        time.sleep(5)
        # isi username
        browser.find_element(
            By.XPATH, "/html/body/div/div[1]/div/div[1]/div/div[2]/div[2]/form/div[1]/div/div[2]/input").send_keys("Yantobasna")
        time.sleep(1)
        # isi password
        browser.find_element(
            By.XPATH, "//*[@id='app']/div[1]/div/div[1]/div/div[2]/div[2]/form/div[2]/div/div[2]/input").send_keys("yanto123")
        time.sleep(1)
        # klik buton login
        browser.find_element(
            By.XPATH, "/html/body/div/div[1]/div/div[1]/div/div[2]/div[2]/form/div[3]/button").click()
        time.sleep(5)
        # validasi
        response_message = browser.find_element(
            By.XPATH, "/html/body/div/div[1]/div/div[1]/div/div[2]/div[2]/div/div[1]/div[1]/p").text
        self.assertIn(response_message, 'Invalid credentials')

    def test_05_failed_login_with_blank_username_password(self):
        browser = self.browser
        browser.get("https://opensource-demo.orangehrmlive.com/")  # buka situs
        browser.maximize_window()
        time.sleep(5)
        # isi username
        browser.find_element(
            By.XPATH, "/html/body/div/div[1]/div/div[1]/div/div[2]/div[2]/form/div[1]/div/div[2]/input").send_keys("")
        time.sleep(1)
        # isi password
        browser.find_element(
            By.XPATH, "//*[@id='app']/div[1]/div/div[1]/div/div[2]/div[2]/form/div[2]/div/div[2]/input").send_keys("")
        time.sleep(1)
        # klik buton login
        browser.find_element(
            By.XPATH, "/html/body/div/div[1]/div/div[1]/div/div[2]/div[2]/form/div[3]/button").click()
        time.sleep(5)
        # validasi
        response_message = browser.find_element(
            By.XPATH, "//*[@id='app']/div[1]/div/div[1]/div/div[2]/div[2]/form/div[1]/div/span").text
        self.assertIn(response_message, 'Required')

        response_message = browser.find_element(
            By.XPATH, "//*[@id='app']/div[1]/div/div[1]/div/div[2]/div[2]/form/div[2]/div/span").text
        self.assertIn(response_message, 'Required')

    def tearDown(self):
        self.browser.close()


if __name__ == "__main__":
    unittest.main()
