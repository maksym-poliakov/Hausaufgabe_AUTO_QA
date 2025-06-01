import time

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.common.exceptions import NoSuchElementException

link_site = "https://itcareerhub.de/ru"


@pytest.fixture(params=["chrome"])
def driver(request):
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    yield driver
    driver.quit()

def test_open_ich(driver):
    #Решение
    driver.get(link_site)
    assert "Начните IT-карьеру в Германии" in driver.title, "Начните IT-карьеру в Германии"

def test_logo(driver):
    driver.get(link_site)

    logo = driver.find_element( By.XPATH,"/html/body/div[1]/div[5]/div/div/div[11]/a/img")
    assert logo is not None,"element logo not found"

def test_link_programs(driver):
    driver.get(link_site)
    program = driver.find_element(By.CSS_SELECTOR,"div.t396__elem.tn-elem.tn-elem__7178437221709552454448 > a")
    assert program.text == "Программы"

def test_link_payment(driver):
    driver.get(link_site)
    payment = driver.find_element(By.CSS_SELECTOR,"div.t396__elem.tn-elem.tn-elem__7178437221709552445907 > a")
    assert payment.text == "Способы оплаты"

def test_link_news(driver):
    driver.get(link_site)
    news = driver.find_element(By.CSS_SELECTOR, "div.t396__elem.tn-elem.tn-elem__7178437221709552475577 > a")
    assert news.text == "Новости"

def test_about_us(driver):
    driver.get(link_site)
    about_us = driver.find_element(By.CSS_SELECTOR,"div.t396__elem.tn-elem.tn-elem__7178437221709552503050 > a")
    assert about_us.text == "О нас"

def test_reviews(driver):
    driver.get(link_site)
    reviews = driver.find_element(By.CSS_SELECTOR,"div.t396__elem.tn-elem.tn-elem__7178437221709552523895 > a")
    assert reviews.text == "Отзывы"


def test_ru(driver):
    driver.get(link_site)
    language_ru = driver.find_element(By.CSS_SELECTOR,"div.t396__elem.tn-elem.tn-elem__7178437221710153064158")
    assert language_ru is not None , "element ru not found"


def test_de(driver):
    driver.get(link_site)
    language_de = driver.find_element(By.CSS_SELECTOR, "div.t396__elem.tn-elem.tn-elem__7178437221710153064158")
    assert language_de is not None, "element de not found"

def test_clic_phone(driver):
    driver.get(link_site)
    phone = driver.find_element(By.CSS_SELECTOR,"div.t396__elem.tn-elem.tn-elem__7178437221710153310161 > a > img")
    phone.click()
    time.sleep(1)
    modal = driver.find_element(By.CSS_SELECTOR,"div.t396__elem.tn-elem.tn-elem__7679561671711363912027 > div")
    assert modal.text == "Если вы не дозвонились, заполните форму на сайте. Мы свяжемся с вами"




