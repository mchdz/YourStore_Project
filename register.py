import time
import unittest
import HtmlTestRunner
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select


class Register_page(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.maximize_window()

    def test_register(self):
        driver = self.driver
        driver.get("https://opencart.abstracta.us/index.php?route=account/register")
        driver.find_element(By.XPATH, "/html[1]/body[1]/nav[1]/div[1]/div[2]/ul[1]/li[2]/a[1]").click()
        driver.find_element(By.LINK_TEXT, "Register").click()
        time.sleep(5)
        driver.find_element(By.XPATH, "/html[1]/body[1]/div[2]/div[1]/div[1]/form[1]/fieldset[1]/div[2]/div[1]/input[1]"
                            ).send_keys("Marcell")
        time.sleep(1)
        driver.find_element(By.XPATH, "/html[1]/body[1]/div[2]/div[1]/div[1]/form[1]/fieldset[1]/div[3]/div[1]/input[1]"
                            ).send_keys("Castro")
        time.sleep(1)
        driver.find_element(By.XPATH, "/html[1]/body[1]/div[2]/div[1]/div[1]/form[1]/fieldset[1]/div[4]/div[1]/input[1]"
                            ).send_keys("marcell.chdz@gmail.com")
        time.sleep(1)
        driver.find_element(By.XPATH, "/html[1]/body[1]/div[2]/div[1]/div[1]/form[1]/fieldset[1]/div[5]/div[1]/input[1]"
                            ).send_keys("66729324323")
        time.sleep(1)
        driver.find_element(By.XPATH, "/html[1]/body[1]/div[2]/div[1]/div[1]/form[1]/fieldset[2]/div[1]/div[1]/input[1]"
                            ).send_keys("metallica00")
        time.sleep(1)
        driver.find_element(By.XPATH, "/html[1]/body[1]/div[2]/div[1]/div[1]/form[1]/fieldset[2]/div[2]/div[1]/input[1]"
                            ).send_keys("metallica00")
        time.sleep(1)
        driver.find_element(By.XPATH, "/html[1]/body[1]/div[2]/div[1]/div[1]/form[1]/fieldset[3]/div[1]/div[1]/label["
                                      "2]/input[1]").click()
        time.sleep(1)
        driver.find_element(By.XPATH, "/html[1]/body[1]/div[2]/div[1]/div[1]/form[1]/div[1]/div[1]/input[1]").click()
        driver.find_element(By.XPATH, "/html[1]/body[1]/div[2]/div[1]/div[1]/form[1]/div[1]/div[1]/input[2]").click()
        driver.save_screenshot('Usuario registrado correctamente.png')
        time.sleep(5)



    def tearDown(self):
        driver = self.driver
        driver.close()


if __name__ == '__main__':
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output="Resultados de testing Registro"))
