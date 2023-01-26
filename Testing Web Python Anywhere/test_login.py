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
        browser = self.browser  # buka web browser
        browser.get("http://barru.pythonanywhere.com/daftar")  # buka situs
        time.sleep(3)
        browser.find_element(
            By.XPATH, "/html/body/div/div[2]/form/input[1]").send_keys("tester@jagoqa.com")  # isi email
        time.sleep(1)
        browser.find_element(By.CSS_SELECTOR, "input#password").send_keys(
            "testerjago")  # isi password
        time.sleep(1)
        # klik tombol sign in
        browser.find_element(By.ID, "signin_login").click()
        time.sleep(1)
        # validasi
        response_data = browser.find_element(By.ID, "swal2-title").text
        response_message = browser.find_element(By.ID, "swal2-content").text

        self.assertIn('Welcome', response_data)
        self.assertEqual(response_message, 'Anda Berhasil Login')

    def test_02_failed_login_invalid_email(self):
        # steps
        # buka web browser
        browser = self.browser
        # buka situs
        browser.get("http://barru.pythonanywhere.com/daftar")
        time.sleep(3)
        # isi email
        browser.find_element(
            By.XPATH, "/html/body/div/div[2]/form/input[1]").send_keys("jagoanku@gmail.com")
        time.sleep(1)
        # isi password
        browser.find_element(
            By.CSS_SELECTOR, "input#password").send_keys("testerjago")
        time.sleep(1)
        # klik tombol sign in
        browser.find_element(By.ID, "signin_login").click()
        time.sleep(1)
        # validasi
        response_data = browser.find_element(By.ID, "swal2-title").text
        response_message = browser.find_element(By.ID, "swal2-content").text

        self.assertIn("User's not found", response_data)
        self.assertEqual(response_message, 'Email atau Password Anda Salah')

    def test_03_failed_login_invalid_password(self):
        # steps
        # buka web browser
        browser = self.browser
        # buka situs
        browser.get("http://barru.pythonanywhere.com/daftar")
        time.sleep(3)
        # isi email
        browser.find_element(
            By.XPATH, "/html/body/div/div[2]/form/input[1]").send_keys("tester@jagoqa.com")
        time.sleep(1)
        # isi password
        browser.find_element(
            By.CSS_SELECTOR, "input#password").send_keys("12345")
        time.sleep(1)
        # klik tombol sign in
        browser.find_element(By.ID, "signin_login").click()
        time.sleep(1)
        # validasi
        response_data = browser.find_element(By.ID, "swal2-title").text
        response_message = browser.find_element(By.ID, "swal2-content").text

        self.assertIn("User's not found", response_data)
        self.assertEqual(response_message, 'Email atau Password Anda Salah')

    def test_04_failed_login_invalid_email_and_password(self):
        # steps
        # buka web browser
        browser = self.browser
        # buka situs
        browser.get("http://barru.pythonanywhere.com/daftar")
        time.sleep(3)
        # isi email
        browser.find_element(
            By.XPATH, "/html/body/div/div[2]/form/input[1]").send_keys("jagoan@jagoenakenak.com")
        time.sleep(1)
        # isi password
        browser.find_element(
            By.CSS_SELECTOR, "input#password").send_keys("jago123")
        time.sleep(1)
        # klik tombol sign in
        browser.find_element(By.ID, "signin_login").click()
        time.sleep(1)
        # validasi
        response_data = browser.find_element(By.ID, "swal2-title").text
        response_message = browser.find_element(By.ID, "swal2-content").text

        self.assertIn("User's not found", response_data)
        self.assertEqual(response_message, 'Email atau Password Anda Salah')

    def test_05_failed_login_with_blank_email_and_password(self):
        # steps
        # buka web browser
        browser = self.browser
        # buka situs
        browser.get("http://barru.pythonanywhere.com/daftar")
        time.sleep(3)
        # isi email
        browser.find_element(
            By.XPATH, "/html/body/div/div[2]/form/input[1]").send_keys("")
        time.sleep(1)
        # isi password
        browser.find_element(By.ID, "password").send_keys("")
        time.sleep(1)
        # klik tombol sign in
        browser.find_element(By.ID, "signin_login").click()
        time.sleep(1)

        # validasi
        response_data = browser.find_element(By.ID, "swal2-title").text
        response_message = browser.find_element(By.ID, "swal2-content").text

        self.assertIn("User's not found", response_data)
        self.assertEqual(response_message, 'Email atau Password Anda Salah')

    def tearDown(self):
        self.browser.close()


if __name__ == "__main__":
    unittest.main()
