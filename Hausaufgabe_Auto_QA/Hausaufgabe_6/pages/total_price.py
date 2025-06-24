from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class TotalPrice:
    def __init__(self,driver):
        self.driver = driver
        self.wait = WebDriverWait(driver,10)

    def get_total_price(self):
        return self.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR,
                              "#checkout_summary_container > div > div.summary_info > div.summary_total_label"))).text