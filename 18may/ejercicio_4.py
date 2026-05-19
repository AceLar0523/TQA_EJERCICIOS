import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
driver.maximize_window()

try:
    driver.get("https://demoqa.com/browser-windows")
    wait = WebDriverWait(driver, 10)
    
    main_window = driver.current_window_handle
    
    tab_button = wait.until(EC.element_to_be_clickable((By.ID, "tabButton")))
    tab_button.click()
    time.sleep(4)
    
    all_windows = driver.window_handles
    for window in all_windows:
        if window != main_window:
            driver.switch_to.window(window)
            break
    
    time.sleep(4)
    heading = wait.until(EC.presence_of_element_located((By.ID, "sampleHeading")))
    heading_text = heading.text
    print(f"\n[INFO] Texto obtenido de la nueva pestaña: '{heading_text}'")
    
    driver.close()
    driver.switch_to.window(main_window)
    time.sleep(4)
    
    assert "sample" in heading_text.lower()
    print("TEST DE EJECUCIÓN: PASSED - Flujo de pestañas completado con éxito.")

except Exception as e:
    print(f"TEST DE EJECUCIÓN: FAILED - Error durante la automatización: {e}")
    
finally:
    driver.quit()