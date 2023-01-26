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

    def test_success_logout(self):
        # steps
        # buka web browser
        browser = self.browser
        # buka situs
        browser.get("https://katalon-demo-cura.herokuapp.com/")
        # layar penuh page
        browser.maximize_window()
        time.sleep(3)
        # klik toggle menu
        browser.find_element(By.ID, "menu-toggle").click()
        time.sleep(1)
        # klik login
        browser.find_element(By.XPATH, "/html/body/nav/ul/li[3]/a").click()
        time.sleep(1)
        # isi username
        browser.find_element(By.ID, "txt-username").send_keys("John Doe")
        time.sleep(1)
        # isi password
        browser.find_element(
            By.ID, "txt-password").send_keys("ThisIsNotAPassword")
        time.sleep(1)
        # klik tombol sign in
        browser.find_element(By.ID, "btn-login").click()
        time.sleep(1)
        # klik toogle menu
        browser.find_element(By.ID, "menu-toggle").click()
        time.sleep(1)
        # klik menu logout
        browser.find_element(By.XPATH, "/html/body/nav/ul/li[5]/a").click()
        time.sleep(1)
        # validasi
        expectedURL = "https://katalon-demo-cura.herokuapp.com/"
        actualURL = browser.current_url
        self.assertEquals(expectedURL, actualURL)

    def tearDown(self):
        self.browser.close()


if __name__ == "__main__":
    unittest.main()
