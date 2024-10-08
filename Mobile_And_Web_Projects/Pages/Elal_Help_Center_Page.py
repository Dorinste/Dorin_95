from selenium.webdriver.common.by import By


class help_center_page():
    def __init__(self, web_driver):
        self.web_driver = web_driver
        self.way_to_contact_locator = 'contact - option'

    def get_number_to_dial(self):
        way_to_contact = self.web_driver.find_elements(By.CLASS_NAME, self.way_to_contact_locator)
        elal_phone_number = way_to_contact[2].text
        print(elal_phone_number)
        elal_index = elal_phone_number.index('Sun')
        elal_number = elal_phone_number[:elal_index]
        elal_num = elal_number.replace('-', '')
        print(elal_num)
        final_num_to_dial = elal_num.replace('+', '')
        print(final_num_to_dial)

        return final_num_to_dial