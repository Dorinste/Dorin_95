import unittest
import time
from appium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium import webdriver as web_driver
from Mobile_And_Web_Projects.Tests.Globals import capabilities_mobile, ups_url
from Mobile_And_Web_Projects.Pages.Ups_Help_Center_Page import help_center_page
from Mobile_And_Web_Projects.Pages.dialer_page import dialer_page


class ups_test(unittest.TestCase):
    def setUp(self) -> None:
        appium_server_url_local = 'http://localhost:4723/wd/hub'
        self.mobile_driver = webdriver.Remote(appium_server_url_local, capabilities_mobile)
        self.mobile_driver.implicitly_wait(10)
        service = ChromeService(executable_path=ChromeDriverManager().install())
        self.web_driver = web_driver.Chrome(service=service)
        self.web_driver.implicitly_wait(10)
        self.web_driver.maximize_window()
        self.web_driver.get(ups_url)
        time.sleep(3)
        self.dialer = dialer_page(self.mobile_driver)
        self.help_center = help_center_page(self.web_driver)
        print('test start')

    def tearDown(self) -> None:
        if self.mobile_driver:
            self.mobile_driver.quit()
        if self.web_driver:
           self.web_driver.quit()
        print('test end')

    def test_dial_to_ups(self):
        final_num = self.help_center.get_number_to_dial()
        self.dialer.click_on_key_pad()
        self.dialer.dial_number(final_num)
        self.dialer.click_on_call_button()
        self.dialer.click_on_hang_up()
