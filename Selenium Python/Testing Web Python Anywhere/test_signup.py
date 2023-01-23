import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager


class TestSignUp(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Chrome(ChromeDriverManager().install())

    def test_01_succces_signup(self):
        # buka browser
        browser = self.browser
        # buka situs
        browser.get("http://barru.pythonanywhere.com/daftar")
        # layar penuh page
        browser.maximize_window()
        time.sleep(5)
        # klik tombol signup
        browser.find_element(By.ID, "signUp").click()
        time.sleep(1)
        # isi name
        browser.find_element(
            By.ID, "name_register").send_keys("yanti")
        time.sleep(1)
        # isi email
        browser.find_element(
            By.ID, "email_register").send_keys("yanti@gmail.com")
        time.sleep(1)
        # isi password
        browser.find_element(
            By.ID, "password_register").send_keys("yanti123")
        time.sleep(1)
        # klik tombol signup
        browser.find_element(By.ID, "signup_register").click()
        time.sleep(1)
        # validasi
        response_data = browser.find_element(By.ID, "swal2-title").text
        response_message = browser.find_element(By.ID, "swal2-content").text

        self.assertIn('berhasil', response_data)
        self.assertEqual(response_message, 'User created')

    def test_02_failed_signup_with_blank_name(self):
        # buka browser
        browser = self.browser
        # buka situs
        browser.get("http://barru.pythonanywhere.com/daftar")
        # layar penuh page
        browser.maximize_window()
        time.sleep(5)
        # klik tombol signup
        browser.find_element(By.ID, "signUp").click()
        time.sleep(1)
        # blank name
        browser.find_element(By.ID, "name_register").send_keys("")
        time.sleep(1)
        # isi email
        browser.find_element(By.ID, "email_register").send_keys(
            "yanto@gmail.com")
        time.sleep(1)
        # isi password
        browser.find_element(By.ID, "password_register").send_keys("yanto123")
        # klik tombol signup
        browser.find_element(By.ID, "signup_register").click()
        time.sleep(1)
        time.sleep(1)
        # validasi
        response_data = browser.find_element(By.ID, "swal2-title").text
        response_message = browser.find_element(By.ID, "swal2-content").text

        self.assertIn('Oops...', response_data)
        self.assertEqual(response_message, 'Gagal Register!')

    def test_03_failed_signup_with_blank_email(self):
        # buka browser
        browser = self.browser
        # buka situs
        browser.get("http://barru.pythonanywhere.com/daftar")
        # layar penuh page
        browser.maximize_window()
        time.sleep(5)
        # klik tombol signup
        browser.find_element(By.ID, "signUp").click()
        time.sleep(1)
        # isi name
        browser.find_element(By.ID, "name_register").send_keys("yanto")
        time.sleep(1)
        # blank email
        browser.find_element(By.ID, "email_register").send_keys("")
        time.sleep(1)
        # isi password
        browser.find_element(By.ID, "password_register").send_keys("yanto123")
        time.sleep(1)
        # klik tombol signup
        browser.find_element(By.ID, "signup_register").click()
        time.sleep(1)
        # validasi
        response_data = browser.find_element(By.ID, "swal2-title").text
        response_message = browser.find_element(By.ID, "swal2-content").text

        self.assertIn('Oops...', response_data)
        self.assertEqual(response_message, 'Gagal Register!')

    def test_04_failed_signup_with_blank_password(self):
        # buka browser
        browser = self.browser
        # buka situs
        browser.get("http://barru.pythonanywhere.com/daftar")
        # layar penuh page
        browser.maximize_window()
        time.sleep(5)
        # klik tombol signup
        browser.find_element(By.ID, "signUp").click()
        time.sleep(1)
        # isi name
        browser.find_element(By.ID, "name_register").send_keys("yanto")
        time.sleep(1)
        # isi email
        browser.find_element(By.ID, "email_register").send_keys(
            "yanto@gmail.com")
        time.sleep(1)
        # blank password
        browser.find_element(By.ID, "password_register").send_keys("")
        time.sleep(1)
        # klik tombol signup
        browser.find_element(By.ID, "signup_register").click()
        time.sleep(1)
        # validasi
        response_data = browser.find_element(By.ID, "swal2-title").text
        response_message = browser.find_element(By.ID, "swal2-content").text

        self.assertIn('Oops...', response_data)
        self.assertEqual(response_message, 'Gagal Register!')

    def test_05_failed_signup_blank_field(self):
        # buka browser
        browser = self.browser
        # buka situs
        browser.get("http://barru.pythonanywhere.com/daftar")
        # layar penuh page
        browser.maximize_window()
        time.sleep(5)
        # klik tombol signup
        browser.find_element(By.ID, "signUp").click()
        time.sleep(1)
        # blank name
        browser.find_element(
            By.ID, "name_register").send_keys("")
        time.sleep(1)
        # blank email
        browser.find_element(
            By.ID, "email_register").send_keys("")
        time.sleep(1)
        # blank password
        browser.find_element(
            By.ID, "password_register").send_keys("")
        time.sleep(1)
        # klik tombol signup
        browser.find_element(By.ID, "signup_register").click()
        time.sleep(1)
        # validasi
        response_data = browser.find_element(By.ID, "swal2-title").text
        response_message = browser.find_element(By.ID, "swal2-content").text

        self.assertIn('Oops...', response_data)
        self.assertEqual(response_message, 'Gagal Register!')


def tearDown(self):
    self.browser.close()


if __name__ == "__main__":
    unittest.main()
