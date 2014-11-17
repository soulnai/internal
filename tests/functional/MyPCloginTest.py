'''
Created on Nov 7, 2014

@author: avasilyev2
'''

#stdlib
import unittest
import time

#selenium
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import ActionChains

#pytest
import pytest


class MyPcSwitchViewsTest(unittest.TestCase):

    def setUp(self):
        """Open MyPC Login page and login as user "admin" without password"""
        self.driver = webdriver.Firefox()
        self.wait = WebDriverWait(self.driver, 10)
        self.driver.get("http://10.10.32.66/loadtest")
        assert "Performance Center" in self.driver.title
        login_name_field = self.wait.until(EC.element_to_be_clickable((By.ID, 'ctl00_PageContent_txtUserName')))
        login_name_field.send_keys("admin")
        login_name_field.send_keys(Keys.RETURN)
        login_button = self.wait.until(EC.element_to_be_clickable((By.ID, 'ctl00_PageContent_btnLogin')))
        login_button.click()
        time.sleep(5)
        self.driver.switch_to.window(self.driver.window_handles[-1])

    def tearDown(self):
        self.driver.quit()

    def test_switch_to_test_plan_perspective(self):
        """Switch to test plan perspective after login"""
        driver = self.driver
        wait = WebDriverWait(driver, 10)
        test_perspective_button = wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/masthead/div/div[3]/div/div[2]/span[1]")))
        actions = ActionChains(driver)
        actions.move_to_element(test_perspective_button)
        actions.perform()
        time.sleep(2)
        actions2 = ActionChains(driver)
        test_plan = wait.until(EC.presence_of_element_located((By.XPATH, "/html/body/masthead/div/div[3]/div/div[2]/ul/li[1]")))
        actions2.move_to_element(test_plan)
        actions2.click(test_plan)
        actions2.perform()
        time.sleep(5)
        #test_plan.click()


"""if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    pytest.main()
"""