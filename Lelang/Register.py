import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager


class TestRegister(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Chrome(ChromeDriverManager().install())

    def test_success_register(self):
        browser = self.browser
        browser.get("https://banknawadata.com/")  # buka situs
        browser.maximize_window()
        time.sleep(5)
        # isi nama lengkap
        browser.find_element(By.ID, "name_id").send_keys("Iqbal")
        time.sleep(1)
        # isi Email
        browser.find_element(By.ID, "email_id").send_keys("Iqbal123")
        time.sleep(1)
        # isi Alamat
        browser.find_element(By.ID, "alamat_id").send_keys("Jombang")
        time.sleep(1)
        # klik dropdown provinsi
        browser.find_element(By.XPATH, "/html/body/div/div[1]/div/div[1]/div/div[2]/div[2]/form/div[3]/i").click()
        time.sleep(2)
        # pilih item dropdown provinsi
        browser.find_element(By.XPATH, "/html/body/div/div[1]/div/div[1]/div/div[2]/div[2]/form/div[3]/div[1]").click()
        time.sleep(2)
        # klik dropdown kabupaten
        browser.find_element(By.XPATH, "/html/body/div/div[1]/div/div[1]/div/div[2]/i").click()
        time.sleep(2)
        # pilih item dropdown kabupaten
        browser.find_element(By.XPATH, "/html/body/div/div[1]/div/div[1]/div/div[2]").click()
        time.sleep(2)
        # isi kode pos
        browser.find_element(By.ID, "kodepos_id").send_keys("61456")
        time.sleep(1)
        # klik dropdown kartu identitas
        browser.find_element(By.XPATH, "/html/body/div/div[1]/div/div[1]/div/div[2]/i").click()
        time.sleep(2)
        # pilih item dropdown identitas
        browser.find_element(By.XPATH, "/html/body/div/div[1]/div/div[1]/div/div[2]").click()
        time.sleep(2)
        # isi nomer identitas
        browser.find_element(By.ID, "notas_id").send_keys("345671891030")
        time.sleep(1)
        # klik Choose file identitas
        browser.find_element(By.XPATH, "/html/body/div/div[1]/div/div[1]").click()
        self.choose_file("#file-upload", file_path)
        file_path = './downloads/ktp.jpg'
        time.sleep(2)
        # klik choose NPWP
        rowser.find_element(By.XPATH, "/html/body/div/div[1]/div/div[1]").click()
        self.choose_file("#file-upload", file_path)
        file_path = './downloads/npwp.jpg'
        time.sleep(2)
        # isi No HP
        browser.find_element(By.ID, "notelp_id").send_keys("08678923456")
        time.sleep(1)
        # klik dropdown kartu debit
        browser.find_element(By.XPATH, "/html/body/div/div[1]/div/div[1]/div/div[2]/i").click()
        time.sleep(2)
        # pilih item dropdown kartu debit
        browser.find_element(By.XPATH, "/html/body/div/div[1]/div/div[1]/div/div[2]").click()
        time.sleep(2)
        # isi No Rekening
        browser.find_element(By.ID, "norekening_id").send_keys("33333678678923456")
        time.sleep(1)
        # isi Nama Rekening
        browser.find_element(By.ID, "rekening_id").send_keys("M Iqbal Harisuddin")
        time.sleep(1)
        # isi Password
        browser.find_element(By.ID, "pass_id").send_keys("iqbal123")
        time.sleep(1)
        # isi Nama Rekening
        browser.find_element(By.ID, "repeatpass_id").send_keys("iqbal123")
        time.sleep(1)
        # klik cekbox bukan robot
        browser.find_element(By.XPATH, "/html/body/div/div[1]/div/div[1]/div/div[2]").click()
        time.sleep(2)
        # klik pernyataan benar
        browser.find_element(By.XPATH, "/html/body/div/div[1]/div/div[1]/div/div[3]").click()
        time.sleep(2)
        # klik menyetujui ketentuan
        browser.find_element(By.XPATH, "/html/body/div/div[1]/div/div[1]/div/div[4]").click()
        time.sleep(2)
        # klik tombol Daftar
        browser.find_element(By.ID, "daftar_btn").click()
        time.sleep(2)
        # validasi
        response_data = browser.find_element(By.ID, "swal2-title").text
        response_message = browser.find_element(By.ID, "swal2-content").text

        self.assertIn('Welcome', response_data)
        self.assertEqual(response_message, 'Anda Berhasil Login')

    def tearDown(self):
        self.browser.close()


if __name__ == "__main__":
    unittest.main()
