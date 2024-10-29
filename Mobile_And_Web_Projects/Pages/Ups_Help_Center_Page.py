from selenium.webdriver.common.by import By


class help_center_page():
    def __init__(self, web_driver):
        self.web_driver = web_driver

    def get_number_to_dial(self):
        contacts = self.web_driver.find_elements(By.CLASS_NAME, 'ups-analytics.ups-cta.ups-cta-secondary')
        ups_phone_number = contacts[0].text
        print(ups_phone_number)
        ups_num = ups_phone_number.replace('-', '')
        print(ups_num)
        final_num_to_dial = ups_num.replace('+', '')
        print(f'this is UPS final number to dial', final_num_to_dial)

        return final_num_to_dial
