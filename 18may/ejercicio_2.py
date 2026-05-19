import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
driver.maximize_window()

try:
    driver.get("https://the-internet.herokuapp.com/login")
    wait = WebDriverWait(driver, 10)
    
    username_input = wait.until(EC.presence_of_element_located((By.XPATH, "//input[contains(@id, 'username')]")))
    password_input = driver.find_element(By.XPATH, "//input[contains(@id, 'password')]")
    login_button = driver.find_element(By.XPATH, "//button[contains(@type, 'submit')]")
    
    username_input.send_keys("alex_dev_incorrecto")
    password_input.send_keys("password_falso_123")
    
    login_button.click()
    
    error_alert = wait.until(
        EC.presence_of_element_located((By.XPATH, "//div[contains(@id, 'flash') and contains(@class, 'error')]"))
    )
    
    alert_text = error_alert.text.strip()
    print(f"\n[INFO] Mensaje capturado en pantalla: '{alert_text}'")
    
    assert "invalid" in alert_text.lower(), "¡El mensaje de error no contiene el texto esperado!"
    print("TEST DE EJECUCIÓN: PASSED - Alerta de error validada correctamente.")

except Exception as e:
    print(f"TEST DE EJECUCIÓN: FAILED - Error durante la automatización: {e}")
    
finally:
    driver.quit()