import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager


class TestViewList(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Chrome(ChromeDriverManager().install())

    def test_tawar(self):
        browser = self.browser
        browser.get("https://banknawadata.com/")  # buka situs
        browser.maximize_window()
        time.sleep(5)
        # klik view lot
        browser.find_element(By.ID, "lot_id").click()
        time.sleep(2)
        # klik plus button
        browser.find_element(By.ID, "plus_id").click()
        time.sleep(2)
        # klik tawar button
        browser.find_element(By.ID, "tawar_id").click()
        time.sleep(2)
        # klik info detail button
        browser.find_element(By.ID, "detail_id").click()
        time.sleep(2)
        # validasi
        expectedURL = "https://banknawadata.com/view/lot"
        actualURL = browser.current_url
        self.assertEquals(expectedURL, actualURL)

    def test_tawar_otomatis(self):
        browser = self.browser
        browser.get("https://banknawadata.com/")  # buka situs
        browser.maximize_window()
        time.sleep(5)
        # input Kode LOT
        browser.find_element(By.XPATH, "lot_id").send_keys("LOT002")
        time.sleep(2)
        # klik view lot
        browser.find_element(By.XPATH, "lot_btn").click()
        time.sleep(2)
        # klik tawar otomatis button
        browser.find_element(By.ID, "tawar_btn").click()
        time.sleep(2)
        # klik info detail button
        browser.find_element(By.ID, "detail_btn").click()
        time.sleep(2)
        # validasi
        expectedURL = "https://banknawadata.com/view/lot"
        actualURL = browser.current_url
        self.assertEquals(expectedURL, actualURL)

    def tearDown(self):
        self.browser.close()


if __name__ == "__main__":
    unittest.main()
