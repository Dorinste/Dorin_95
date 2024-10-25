import time
from appium.webdriver.common.appiumby import AppiumBy


class dialer_page:
    def __init__(self, mobile_driver):
        self.mobile_driver = mobile_driver
        self.dialer_locator = 'com.google.android.apps.nexuslauncher:id/overview_actions_view'
        self.key_pad_locator = 'com.google.android.dialer:id/dialpad_fab'
        self.call_button_locator = 'com.google.android.dialer:id/dialpad_voice_call_button'
        self.hanging_up_locator = 'com.google.android.dialer:id/incall_end_call'

    def click_on_key_pad(self):
        time.sleep(3)
        key_pad = self.mobile_driver.find_element(by=AppiumBy.ID, value=self.key_pad_locator)
        key_pad.click()

    def dial_number(self, num_to_dial):
        print(f'dialing to number ', num_to_dial)
        for digit in num_to_dial:
            print(f'Trying to click on digit', digit)
            match digit:
                case '1':
                    num = self.mobile_driver.find_element(by=AppiumBy.ID, value='com.google.android.dialer:id/one')
                case '2':
                    num = self.mobile_driver.find_element(by=AppiumBy.ID, value='com.google.android.dialer:id/two')
                case '3':
                    num = self.mobile_driver.find_element(by=AppiumBy.ID, value='com.google.android.dialer:id/three')
                case '4':
                    num = self.mobile_driver.find_element(by=AppiumBy.ID, value='com.google.android.dialer:id/four')
                case '5':
                    num = self.mobile_driver.find_element(by=AppiumBy.ID, value='com.google.android.dialer:id/five')
                case '6':
                    num = self.mobile_driver.find_element(by=AppiumBy.ID, value='com.google.android.dialer:id/six')
                case '7':
                    num = self.mobile_driver.find_element(by=AppiumBy.ID, value='com.google.android.dialer:id/seven')
                case '8':
                    num = self.mobile_driver.find_element(by=AppiumBy.ID, value='com.google.android.dialer:id/eight')
                case '9':
                    num = self.mobile_driver.find_element(by=AppiumBy.ID, value='com.google.android.dialer:id/nine')
                case '0':
                    num = self.mobile_driver.find_element(by=AppiumBy.ID, value='com.google.android.dialer:id/zero')
            num.click()

    def click_on_call_button(self):
        call_button = self.mobile_driver.find_element(by=AppiumBy.ID, value=self.call_button_locator)
        call_button.click()

    def click_on_hang_up(self):
        hanging_up = self.mobile_driver.find_element(by=AppiumBy.ID, value=self.hanging_up_locator)
        hanging_up.click()
