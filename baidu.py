# -*- coding:utf8 -*-
from selenium import webdriver
import unittest
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities


class baidu(unittest.TestCase):
    def setUp(self):
        # options = webdriver.ChromeOptions()
        # options.binary_location = 'G:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe'
        # self.driver = webdriver.Chrome('D:\\a_gitlab\\auto\\chromedriver.exe', chrome_options = options)
        options = Options()
        options.binary = r'C:\\Program Files\\Mozilla Firefox\\firefox.exe'
        cap = DesiredCapabilities().FIREFOX
        cap["marionette"] = True
        self.driver = webdriver.Firefox(firefox_options=options, capabilities=cap, executable_path="D:\\a_gitlab\\auto\\geckodriver.exe")

    def test_open(self):
        self.driver.get('https://www.baidu.com')
        # print()
        self.assertEqual(self.driver.title, u'百度一下，你就知道')
    
    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()
