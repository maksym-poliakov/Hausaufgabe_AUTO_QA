from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class YouInformationPage:

    def __init__(self,driver):
        self.driver = driver
        self.wait = WebDriverWait(driver,10)

    def get_firstname_input(self):
        return self.wait.until(EC.presence_of_element_located((By.XPATH,'//*[@id="first-name"]')))

    def get_lastname_input(self):
        return self.wait.until(EC.presence_of_element_located((By.XPATH,'//*[@id="last-name"]')))

    def get_zipcode_input(self):
        return self.wait.until(EC.presence_of_element_located((By.XPATH,'//*[@id="postal-code"]')))

    def go_to_overview(self):
        self.wait.until(EC.element_to_be_clickable((By.XPATH,'//*[@id="continue"]'))).click()

    def enter_firstname(self,firstname):
        firstname_field = self.get_firstname_input()
        firstname_field.clear()
        firstname_field.send_keys(firstname)

    def enter_lastname(self,lastname):
        lastname_field = self.get_lastname_input()
        lastname_field.clear()
        lastname_field.send_keys(lastname)

    def enter_zipcode(self,zipcode):
        zipcode_field = self.get_zipcode_input()
        zipcode_field.clear()
        zipcode_field.send_keys(zipcode)