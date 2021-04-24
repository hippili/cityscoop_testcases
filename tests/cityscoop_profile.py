import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException


class cityscoop_profile(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()

    def test_nca(self):
        user = "su"
        pwd = "Maverick1a"
        driver = self.driver
        driver.maximize_window()
        driver.get("https://cityscoop.netlify.app/")
        elem = driver.find_element_by_id("input-1")
        elem.send_keys(user)
        elem = driver.find_element_by_id("input-3")
        elem.send_keys(pwd)
        elem.send_keys(Keys.RETURN)
        driver.find_element_by_xpath("//*[@id='signup']/center/div/div/div/form/div[3]/button").click()
        assert "Logged In"
        time.sleep(2)
        elem = driver.find_element_by_xpath("/html/body/div/div/center/div[1]/input")
        elem.send_keys("Omaha")
        driver.find_element_by_xpath("//*[@id='app']/div/center/div[1]/button").click()
        time.sleep(2)
        driver.find_element_by_xpath("//*[@id='header']/div/nav/ul/li[3]/a/a").click()
        time.sleep(2)
