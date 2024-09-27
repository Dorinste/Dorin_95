from selenium.webdriver.common.by import By


class help_center_page():
    def __init__(self, web_driver):
        self.web_driver = web_driver
        self.way_to_contact_locator = 'ups-analytics ups-cta ups-cta-secondary'

    def get_number_to_dial(self):
        way_to_contact = self.web_driver.find_elements(By.CLASS_NAME,self.way_to_contact_locator)

        ups_phone_number = way_to_contact[2].text
        print(ups_phone_number)
        ups_num = ups_phone_number.replace('-', '')
        print(ups_num)
        final_num_to_dial = ups_num.replace('+', '')
        print(final_num_to_dial)

        return final_num_to_dial

