import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from pages.products_page import  ProductPage
from pages.login_page import LoginPage
from pages.basket_page import BasketPage
from pages.you_information_page import YouInformationPage
from pages.total_price import TotalPrice
from selenium.webdriver.chrome.options import Options

class BaseTest:
    @pytest.fixture(autouse=True)
    def setup(self):
        chrome_options = Options()
        chrome_options.add_argument("--disable-infobars")
        chrome_options.add_argument("--disable-notifications")
        chrome_options.add_experimental_option("prefs", {
            "credentials_enable_service": False,
            "profile.password_manager_enabled": False
        })

        self.driver = webdriver.Chrome(
            service=ChromeService(ChromeDriverManager().install()),
            options=chrome_options
        )
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.driver.maximize_window()
        self.driver.get("https://www.saucedemo.com/")

        self.wait = WebDriverWait(self.driver,10)
        self.login_page = LoginPage(self.driver)
        self.product_page = ProductPage(self.driver)
        self.basket_page = BasketPage(self.driver)
        self.you_information_page = YouInformationPage(self.driver)
        self.total_price_page = TotalPrice(self.driver)

        yield
        self.driver.quit()

    def get_browser_name(self):
        browser_name = self.driver.capabilities['browserName']
        return f"{browser_name} "

