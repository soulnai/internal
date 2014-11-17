'''
Created on Nov 7, 2014

@author: avasilyev2
'''

#stdlib
import unittest
import os
import time

#selenium
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities


class LohikaReferralBonusCheck(unittest.TestCase):

    def setUp(self):
        '''
        Prepare Selenium remote driver.
        Open company-development page
        '''
        self.driver = webdriver.Remote("http://217.146.255.21:4444/wd/hub", desired_capabilities={'browserName': 'htmlunit',
                        'version': '2', 'javascriptEnabled': True})
        self.wait = WebDriverWait(self.driver, 10)
        self.driver.get("http://www.lohika.com.ua/#company-development")

    def tearDown(self):
        self.driver.quit()

    def check_if_text_present(self):
        assert "РОЗРОБКА ДЛЯ МОБІЛЬНИХ ПРИСТРОЇВ" in self.driver.page_source


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()