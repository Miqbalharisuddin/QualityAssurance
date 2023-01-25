import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager


class TestAddproduct(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Chrome(ChromeDriverManager().install())

    def test_add_product(self):
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
        # klik add product
        browser.find_element(By.ID, "add-to-cart-sauce-labs-backpack").click()
        time.sleep(1)
        # klik add product
        browser.find_element(
            By.ID, "add-to-cart-sauce-labs-bike-light").click()
        time.sleep(1)
        # klik menu cart
        browser.find_element(By.ID, "shopping_cart_container").click()
        time.sleep(2)
        # klik checkout
        browser.find_element(By.ID, "checkout").click()
        time.sleep(2)
        # input first name
        browser.find_element(By.ID, "first-name").send_keys("iqbal")
        time.sleep(1)
        # input last name
        browser.find_element(By.ID, "last-name").send_keys("armain")
        time.sleep(1)
        # input kode pos
        browser.find_element(By.ID, "postal-code").send_keys("61465")
        time.sleep(1)
        # klik continue
        browser.find_element(By.ID, "continue").click()
        time.sleep(2)
        # klik finish
        browser.find_element(By.ID, "finish").click()
        time.sleep(2)

        # validasi
        expectedURL = "https://www.saucedemo.com/checkout-complete.html"
        actualURL = browser.current_url
        self.assertEquals(expectedURL, actualURL)

    def tearDown(self):
        self.browser.close()


if __name__ == "__main__":
    unittest.main()
