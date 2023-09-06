import time
import unittest
import HtmlTestRunner
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select


class Addcart(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.maximize_window()

    def test_addArticle(self):
        driver = self.driver
        driver.get("http://opencart.abstracta.us/")
        driver.find_element(By.XPATH, "/html[1]/body[1]/nav[1]/div[1]/div[2]/ul[1]/li[2]/a[1]").click()
        driver.find_element(By.LINK_TEXT, "Login").click()
        time.sleep(2)
        driver.find_element(By.CSS_SELECTOR, "#input-email").send_keys(
            "marcell.chdz@gmail.com" + Keys.TAB + "metallica00")
        time.sleep(2)
        driver.find_element(By.XPATH,
                            "/html[1]/body[1]/div[2]/div[1]/div[1]/div[1]/div[2]/div[1]/form[1]/input[1]").click()
        driver.find_element(By.LINK_TEXT, "Your Store").click()
        time.sleep(2)
        driver.find_element(By.XPATH, "/html[1]/body[1]/div[2]/div[1]/div[1]/div[2]/div[1]/div[1]/div[3]/button["
                                      "1]/span[1]").click()
        time.sleep(2)
        driver.find_element(By.XPATH,
                            "/html[1]/body[1]/div[2]/div[2]/div[1]/div[2]/div[2]/div[1]/div[3]/button[1]").click()
        time.sleep(2)
        driver.find_element(By.XPATH,"/html[1]/body[1]/header[1]/div[1]/div[1]/div[3]/div[1]/button[1]").click()
        driver.find_element(By.XPATH, "/html[1]/body[1]/header[1]/div[1]/div[1]/div[3]/div[1]/ul[1]/li[2]/div[1]/p["
                                      "1]/a[1]/strong[1]").click()
        time.sleep(2)
        driver.find_element(By.XPATH,"/html[1]/body[1]/div[2]/div[2]/div[1]/form[1]/div[1]/table[1]/tbody[1]/tr["
                                     "1]/td[4]/div[1]/span[1]/button[2]/i[1]").click()
        driver.save_screenshot('Añadido al carro exitosamente.png')

        time.sleep(2)



    def tearDown(self):
        driver = self.driver
        driver.close()


if __name__ == '__main__':
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output="Resultados de testing AddCart"))
