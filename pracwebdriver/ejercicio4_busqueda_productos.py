from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.maximize_window()

try:
    driver.get("https://automationexercise.com")

    driver.find_element(
        By.XPATH,
        "//a[contains(text(),'Products')]"
    ).click()

    time.sleep(2)

    driver.find_element(By.ID, "search_product").send_keys("Blue Top")

    driver.find_element(
        By.ID,
        "submit_search"
    ).click()

    time.sleep(2)

    titulo = driver.find_element(
        By.CSS_SELECTOR,
        ".title.text-center"
    )

    # ASSERT 1
    assert titulo.is_displayed()

    productos = driver.find_elements(
        By.XPATH,
        "//div[@class='productinfo text-center']/p"
    )

    encontrado = False

    for producto in productos:
        if "Blue Top" in producto.text:
            encontrado = True
            break

    # ASSERT 2
    assert encontrado

    driver.save_screenshot("ejercicio4_busqueda_producto.png")

    print("Ejercicio 4 aprobado")

finally:
    driver.quit()