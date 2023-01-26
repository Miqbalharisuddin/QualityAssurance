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

    def test_appointment(self):
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
        # pilih facility
        dropMenu = browser.find_element(By.ID, "combo_facility")
        dropMenu.click()
        dropMenu.send_keys("Hongkong CURA Healthcare Center")
        time.sleep(1)
        # klik checkbox
        browser.find_element(By.ID, "chk_hospotal_readmission").click()
        time.sleep(1)
        # klik radiobutton
        browser.find_element(By.ID, "radio_program_medicaid").click()
        time.sleep(1)
        # isi tanggal
        browser.find_element(
            By.ID, "txt_visit_date").send_keys("26 11 2022")
        time.sleep(1)
        # isi comment
        browser.find_element(
            By.ID, "txt_comment").send_keys("Poli Rematologi")
        time.sleep(1)
        # klik book appointment
        browser.find_element(By.ID, "btn-book-appointment").click()
        time.sleep(1)
        # klik toggle menu
        browser.find_element(By.ID, "menu-toggle").click()
        time.sleep(1)
        # klik history
        browser.find_element(By.XPATH, "/html/body/nav/ul/li[3]/a").click()
        time.sleep(1)
        # validasi
        expectedURL = "https://katalon-demo-cura.herokuapp.com/history.php#history"
        actualURL = browser.current_url
        self.assertEquals(expectedURL, actualURL)

    def tearDown(self):
        self.browser.close()


if __name__ == "__main__":
    unittest.main()
