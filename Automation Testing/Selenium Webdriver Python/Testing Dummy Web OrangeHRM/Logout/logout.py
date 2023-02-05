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
        # klik dropdown
        dropMenu = browser.find_element(
            By.XPATH, "/html/body/div/div[1]/div[1]/header/div[1]/div[2]/ul/li/span")
        dropMenu.click()
        dropMenu.browser.find_element(
            By.XPATH, "/html/body/div/div[1]/div[1]/header/div[1]/div[2]/ul/li/ul/li[4]/a")
        dropMenu.click()
        time.sleep(2)
        # validasi
        expectedURL = "https://opensource-demo.orangehrmlive.com/"
        actualURL = browser.current_url
        self.assertEquals(expectedURL, actualURL)

    def tearDown(self):
        self.browser.close()


if __name__ == "__main__":
    unittest.main()
