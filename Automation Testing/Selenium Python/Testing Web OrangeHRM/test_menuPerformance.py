import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager


class TestMenuPerformance(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Chrome(ChromeDriverManager().install())

    def test_menuPerformance(self):
        browser = self.browser
        # buka situs
        browser.get(
            "https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
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
        # klik menu performance
        browser.find_element(
            By.XPATH, "/html/body/div/div[1]/div[1]/aside/nav/div[2]/ul/li[7]/a/span").click()
        time.sleep(8)
        # validasi
        expectedURL = "https://opensource-demo.orangehrmlive.com/web/index.php/performance/searchEvaluatePerformanceReview"
        actualURL = browser.current_url
        self.assertEquals(expectedURL, actualURL)

    def tearDown(self):
        self.browser.close()


if __name__ == "__main__":
    unittest.main()
