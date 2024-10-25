from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.common.by import By


class HelpCenterLocators(object):
    Way_To_Connect = (By.CLASS_NAME, "ups-analytics.ups-cta.ups-cta-secondary")


class DialerPageLocators(object):
    Dialer = (AppiumBy.ID, 'com.google.android.apps.nexuslauncher:id/overview_actions_view')