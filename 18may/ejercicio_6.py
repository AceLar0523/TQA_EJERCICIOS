import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
driver.maximize_window()

try:
    driver.get("https://demoqa.com/alerts")
    wait = WebDriverWait(driver, 10)
    
    alert_button = wait.until(EC.presence_of_element_located((By.ID, "alertButton")))
    driver.execute_script("arguments[0].scrollIntoView(true);", alert_button)
    time.sleep(3)
    
    alert_button.click()
    time.sleep(3)
    
    alert = driver.switch_to.alert
    alert_text = alert.text
    print(f"\n[INFO] Mensaje de la alerta: '{alert_text}'")
    
    alert.accept()
    time.sleep(3)
    
    assert "you clicked a button" in alert_text.lower()
    print("TEST DE EJECUCIÓN: PASSED - Alerta gestionada y mensaje verificado sin errores.")

except Exception as e:
    print(f"TEST DE EJECUCIÓN: FAILED - Error durante la automatización: {e}")
    
finally:
    driver.quit()