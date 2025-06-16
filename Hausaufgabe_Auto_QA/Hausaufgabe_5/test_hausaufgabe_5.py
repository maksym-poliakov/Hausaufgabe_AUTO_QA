import time

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

link_aufgabe_1 = 'https://bonigarcia.dev/selenium-webdriver-java/iframes.html'
link_aufgabe_2 = 'https://www.globalsqa.com/demo-site/draganddrop/'

@pytest.fixture
def driver():
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)
    yield driver
    driver.quit()

# Задание 1: Проверка наличия текста в iframe
# Открыть страницу
# Перейти по ссылке: https://bonigarcia.dev/selenium-webdriver-java/iframes.html.
# Проверить наличие текста
# Найти фрейм (iframe), в котором содержится искомый текст.
# Переключиться в этот iframe.
# Найти элемент, содержащий текст "semper posuere integer et senectus justo curabitur.".
# Убедиться, что текст отображается на странице.

def test_text_iframe(driver):


    driver.get(link_aufgabe_1)
    wait = WebDriverWait(driver,10)

    iframe = wait.until(EC.presence_of_element_located((By.ID, "my-iframe")))

    # Переключение на iframe
    driver.switch_to.frame(iframe)

    lead_elements = driver.find_elements(By.CLASS_NAME, "lead")
    text = "semper posuere integer et senectus justo curabitur."
    element = None

    for index, el in enumerate(lead_elements, 1):
        if text in el.text:
            element = el
            break

    if element:
        assert element.is_displayed(), f"Текст '{text}' НЕ отображается на странице."
        print(f"Текст '{text}' отображается на странице.")
    else:
        assert False, f"Текст '{text}' не найден"

    driver.switch_to.default_content()

# Задание 2: Тестирование Drag & Drop (Перетаскивание изображения в корзину)
# Открыть страницу Drag & Drop Demo.
# Перейти по ссылке: https://www.globalsqa.com/demo-site/draganddrop/.
# Выполнить следующие шаги:
# Захватить первую фотографию (верхний левый элемент).
# Перетащить её в область корзины (Trash).
# Проверить, что после перемещения:
# В корзине появилась одна фотография.
# В основной области осталось 3 фотографии.
# Ожидаемый результат:
# Фотография успешно перемещается в корзину.
# Вне корзины остаются 3 фотографии.

def test_drag_drop(driver):
    driver.get(link_aufgabe_2)
    wait = WebDriverWait(driver, 20)
    dialog_window = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR,".fc-cta-consent > p:nth-child(2)")))
    dialog_window.click()

    iframe = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR,
    '#post-2669 > div.twelve.columns > div > div > '
    'div.single_tab_div.resp-tab-content.resp-tab-content-active > p > iframe')))

    driver.switch_to.frame(iframe)

    draggable = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR,'#gallery > li:nth-child(1)')))
    droppable = driver.find_element(By.ID,'trash')

    actions = ActionChains(driver)

    actions.drag_and_drop(draggable,droppable).perform()

    time.sleep(2)

    images = wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, "#gallery li")))
    images_trash = wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, '#trash')))

    assert len(images) == 3 and len(images_trash) == 1 , \
        f"Осталось в галереи {len(images)} в корзине : {len(images_trash)}"







