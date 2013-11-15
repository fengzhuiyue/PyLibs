from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
import unittest, time, re

class Shoelist(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.base_url = "http://m.letao.com/wap/"
        self.verificationErrors = []
    
    def test_shoelist(self):
        driver = self.driver
        driver.get("/wap/?ltsession=6339598349673581")
        driver.find_element_by_link_text("我的乐淘").click()
        driver.find_element_by_link_text("我的订单").click()
    
    def is_element_present(self, how, what):
        try: self.driver.find_element(by=how, value=what)
        except NoSuchElementException, e: return False
        return True
    
    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    unittest.main()
