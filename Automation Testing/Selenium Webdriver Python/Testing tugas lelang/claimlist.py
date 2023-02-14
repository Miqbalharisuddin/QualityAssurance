import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager


class TestClaimlist(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Chrome(ChromeDriverManager().install())

    def test_claimlist(self):
        browser = self.browser
        browser.get("https://banknawadata.com/")  # buka situs
        browser.maximize_window()
        time.sleep(5)
        # klik Claim list
        browser.find_element(By.ID, "claim_list_id").click()
        time.sleep(2)
        # klik submit button
        browser.find_element(By.ID, "submit_btn").click()
        time.sleep(2)
        # validasi
        expectedURL = "https://banknawadata.com/dashboard"
        actualURL = browser.current_url
        self.assertEquals(expectedURL, actualURL)

    def tearDown(self):
        self.browser.close()


if __name__ == "__main__":
    unittest.main()
