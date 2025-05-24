# Написать скрипт, который:
#
# Открывает в браузере Firefox https://itcareerhub.de/ru
#
# Переходит в раздел “Способы оплаты”
#
# Делает скриншот этой секции страницы
#
# В качестве ответа на задание необходимо приложить ссылку на git репозиторий.

from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.firefox.options import Options
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.by import By
import time

options = Options()
options.binary_location = "/usr/bin/firefox"

driver = webdriver.Firefox(
    service=Service(GeckoDriverManager().install()),
    options=options
)

try:
    driver.get("https://itcareerhub.de")
    time.sleep(2)
    payment_link = driver.find_element(By.LINK_TEXT,"Zahlungsarten")
    payment_link.click()
    driver.save_screenshot('itcareerhub_Zahlungsarten')
    time.sleep(5)
finally:
    driver.quit()