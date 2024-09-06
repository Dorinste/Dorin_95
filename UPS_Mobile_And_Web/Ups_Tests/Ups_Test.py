import unittest
import time
from appium import webdriver as mobile_driver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium import webdriver as web_driver


from UPS_Mobile_And_Web.Ups_Tests.Globals import capabilities_mobile, ups_url
from UPS_Mobile_And_Web.Pages.Help_Center_page import help_center_page
from UPS_Mobile_And_Web.Pages.dialer_page import dialer_page


class ups_test(unittest.TestCase):
    def setUp(self) -> None:
        appium_server_url_local = 'http://localhost:4723/wd/hub'
        self.mobile_driver = mobile_driver.Remote(appium_server_url_local,capabilities_mobile)
        self.mobile_driver.implicitly_wait(10)
        service = ChromeService(executable_path=ChromeDriverManager().install())
        self.web_driver = web_driver.Chrome(service=service)
        self.web_driver.implicitly_wait(10)
        self.web_driver.maximize_window()
        self.web_driver.get(ups_url)
        self.web_driver.refresh()
        time.sleep(3)
        self.dialer = dialer_page(mobile_driver)
        self.help_center = help_center_page(self.web_driver)
        print('test start')

    def tearDown(self) -> None:
        if self.mobile_driver:
            self.mobile_driver.quit()
        if self.web_driver:
           self.web_driver.quit()
        print('test end')

    def test_dial_to_ups(self):
        number_to_dial = self.help_center.get_number_to_dial()
        self.dialer.click_on_key_pad()
        self.dialer.dial_number(number_to_dial)
        self.dialer.click_on_call_button()




