import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

link_aufgabe_1 = 'http://uitestingplayground.com/textinput'
link_aufgabe_2 = 'https://bonigarcia.dev/selenium-webdriver-java/loading-images.html'

@pytest.fixture
def driver():
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)
    yield driver
    driver.quit()


def test_text_buton(driver):
    driver.get(link_aufgabe_1)
    wait = WebDriverWait(driver,10)

    field_input = wait.until(EC.presence_of_element_located((By.ID,'newButtonName')))
    field_input.send_keys("ITCH")

    click_button = wait.until(EC.element_to_be_clickable((By.ID,'updatingButton')))
    click_button.click()

    wait.until(EC.text_to_be_present_in_element((By.ID,'updatingButton'),"ITCH"))

    text_button = driver.find_element(By.ID,'updatingButton').text

    assert text_button == "ITCH", 'Кнопка не содержит "ITCH"'

# Тестируемый сайт:
# https://bonigarcia.dev/selenium-webdriver-java/loading-images.html
# Шаги теста:
# Перейдите на сайт Loading Images.
# Дождитесь загрузки всех изображений.
# Получите значение атрибута alt у третьего изображения.
# Убедитесь, что значение атрибута alt равно "award".

def test_image(driver):
    driver.get(link_aufgabe_2)
    wait = WebDriverWait(driver,20)
    driver.implicitly_wait(20)
    wait.until(EC.text_to_be_present_in_element((By.ID,'text'),'Done!'))
    wait.until(EC.presence_of_element_located((By.ID,'image-container')))
    images = wait.until(EC.presence_of_all_elements_located((By.TAG_NAME,'img')))
    for index,im in enumerate(images):
        index_img = 3
        if index == index_img:
            name_alt = wait.until(EC.presence_of_element_located((By.XPATH,'//*[@alt="award"]'))).get_attribute('alt')
            assert name_alt == "award", "Атрибут alt != award "