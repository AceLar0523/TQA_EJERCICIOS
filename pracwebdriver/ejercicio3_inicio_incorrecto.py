from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.maximize_window()

try:
    driver.get("https://automationexercise.com")

    # Ir al login
    driver.find_element(By.XPATH, "//a[contains(text(),'Signup / Login')]").click()

    # Login incorrecto
    driver.find_element(By.NAME, "email").send_keys("prueba@test.com")
    driver.find_element(By.NAME, "password").send_keys("123456")

    driver.find_element(
        By.CSS_SELECTOR,
        "button[data-qa='login-button']"
    ).click()

    time.sleep(2)

    mensaje = driver.find_element(
        By.XPATH,
        "//p[contains(text(),'Your email or password is incorrect!')]"
    )

    # ASSERT 1
    assert mensaje.is_displayed()

    # ASSERT 2
    assert mensaje.text == "Your email or password is incorrect!"

    driver.save_screenshot("ejercicio3_login_incorrecto.png")

    print("Ejercicio 3 aprobado")

finally:
    driver.quit()