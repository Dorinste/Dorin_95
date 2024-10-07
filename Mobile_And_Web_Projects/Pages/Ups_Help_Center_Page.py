from selenium.webdriver.common.by import By
from Mobile_And_Web_Projects.Pages.locators import HelpCenterLocators


class help_center_page():
    def __init__(self, web_driver):
        self.web_driver = web_driver
        self.Way_to_contact = self.web_driver.find_elements(*HelpCenterLocators.Way_To_Connect)

    def get_number_to_dial(self):
        ups_phone_number = self.Way_to_contact[0].text
        print(ups_phone_number)
        ups_num = ups_phone_number.replace('-', '')
        final_num_to_dial = ups_num.replace('+', '')
        print(final_num_to_dial)
#to add print about the number
        return final_num_to_dial

