from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BasketPage:

    def __init__(self,driver):
        self.driver = driver
        self.wait = WebDriverWait(driver,10)


    def get_items(self):
        return self.wait.until(EC.presence_of_all_elements_located((By.CLASS_NAME,'inventory_item_desc')))

    def get_items_amount(self):
        return len(self.get_items())

    def go_to_checkout(self):
        self.wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="checkout"]'))).click()