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


class LohikaReferralBonusCheck(unittest.TestCase):

    def setUp(self):
        """Open referral bonus page"""
        #self.driver = webdriver.Remote("http://localhost:4444/wd/hub", webdriver.DesiredCapabilities.HTMLUNIT)
        username = os.environ["SAUCE_USERNAME"]
        access_key = os.environ["SAUCE_ACCESS_KEY"]
        #capabilities["tunnel-identifier"] = os.environ["TRAVIS_JOB_NUMBER"]
        hub_url = "%s:%s@localhost:4445" % (username, access_key)
        driver = webdriver.Remote(desired_capabilities="", command_executor="http://%s/wd/hub" % hub_url)
        self.wait = WebDriverWait(self.driver, 10)
        self.driver.get("http://www.lohika.com.ua/#vacancies-referral")

    def tearDown(self):
        self.driver.quit()

    def test_referral_total_amount(self):
        """Calculate total referrals $ amount, referrals Type A total amount and referrals type B total amount"""
        sum_referrals = 0
        sum_a_referrals = 0
        sum_b_referrals = 0
        referal_values_containers = self.driver.find_elements_by_xpath(
            './/*[@id="vacancies-referral"]/div[1]/div/div[2]/table/tbody/tr/td')
        for elem in referal_values_containers:
            if elem.text[-1] == '$':
                sum_referrals = sum_referrals + int(elem.text[:-1])
                if elem.get_attribute('class') == 'td-1':
                    sum_a_referrals = sum_a_referrals + int(elem.text[:-1])
                if elem.get_attribute('class') == 'td-last td-2':
                    sum_b_referrals = sum_b_referrals + int(elem.text[:-1])

        print "Total referal $ amount", sum_referrals
        print "Total A type referal $ amount", sum_a_referrals
        print "Total B type referal $ amount", sum_b_referrals

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()

