from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.maximize_window()

try:
    driver.get("https://automationexercise.com")

    driver.find_element(
        By.XPATH,
        "//a[contains(text(),'Contact us')]"
    ).click()

    driver.find_element(By.NAME, "name").send_keys("Alex")
    driver.find_element(By.NAME, "email").send_keys("alex@test.com")
    driver.find_element(By.NAME, "subject").send_keys("Prueba Selenium")
    driver.find_element(By.NAME, "message").send_keys(
        "Mensaje enviado desde Selenium."
    )

    archivo = os.path.abspath("evidencia.txt")

    driver.find_element(
        By.NAME,
        "upload_file"
    ).send_keys(archivo)

    driver.find_element(
        By.CSS_SELECTOR,
        "input[data-qa='submit-button']"
    ).click()

    alerta = driver.switch_to.alert
    alerta.accept()

    mensaje = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located(
            (By.CSS_SELECTOR, ".status.alert.alert-success")
        )
    )

    # ASSERT 1
    assert mensaje.is_displayed()

    # ASSERT 2
    assert "Success!" in mensaje.text

    driver.save_screenshot("ejercicio5_contact_us.png")

    print("Ejercicio 5 aprobado")

finally:
    driver.quit()