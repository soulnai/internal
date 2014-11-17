#! /usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import unicode_literals
'''
Created on Nov 7, 2014

@author: avasilyev2
'''

#stdlib
import unittest
import sys
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

    def test_if_drop_down_expands_correct(self):
        '''
        Click on expand link.
        Check if reqired element is displayed
        '''
        element_drop_down_activate = self.driver.find_element_by_xpath(
            '//*[@id="company-development"]/div[1]/ul/li[1]/a')
        element_drop_down_activate.click()
        element_to_check = self.driver.find_element_by_xpath(
            '//*[@id="company-development"]/div[1]/ul/li[2]/ul[2]/ul[4]/li[1]/span')
        assert element_to_check.is_displayed()
        #string_to_check = "Розробка на платформі S60 з використанням Native C++"
        #assert string_to_check in self.driver.page_source


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()