from appium.webdriver.common.appiumby import AppiumBy


class dialer_page():
    def __init__(self, mobile_driver):
        self.mobile_driver = mobile_driver
        self.dialer_locator = 'com.google.android.apps.nexuslauncher:id/overview_actions_view'
        self.key_pad_locator = 'com.google.android.dialer:id/dialpad_fab'

        num1 = self.mobile_driver.find_element(by=AppiumBy.ID, value='com.google.android.dialer:id/one')
        num2 = self.mobile_driver.find_element(by=AppiumBy.ID, value='com.google.android.dialer:id/two')
        num3 = self.mobile_driver.find_element(by=AppiumBy.ID, value='com.google.android.dialer:id/three')
        num4 = self.mobile_driver.find_element(by=AppiumBy.ID, value='com.google.android.dialer:id/four')
        num5 = self.mobile_driver.find_element(by=AppiumBy.ID, value='com.google.android.dialer:id/five')
        num6 = self.mobile_driver.find_element(by=AppiumBy.ID, value='com.google.android.dialer:id/six')
        num7 = self.mobile_driver.find_element(by=AppiumBy.ID, value='com.google.android.dialer:id/seven')
        num8 = self.mobile_driver.find_element(by=AppiumBy.ID, value='com.google.android.dialer:id/eight')
        num9 = self.mobile_driver.find_element(by=AppiumBy.ID, value='com.google.android.dialer:id/nine')
        num0 = self.mobile_driver.find_element(by=AppiumBy.ID, value='com.google.android.dialer:id/zero')

        self.call_button_locator = 'com.google.android.dialer:id/dialpad_voice_call_button'


    def dial_number(self, num_to_dial):
        print(f'dialing to number', num_to_dial)
        for digit_x in num_to_dial:
            print(digit_x)
            button = self.num + 'digit_x'
            button.click()

    def click_on_call_button(self):
        call_button = self.mobile_driver.find_element(by=AppiumBy.ID, value=self.call_button_locator)
        call_button.click()
