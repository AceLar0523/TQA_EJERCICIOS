import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
driver.maximize_window()

try:
    driver.get("https://automationexercise.com")
    wait = WebDriverWait(driver, 10)
    
    products_link = wait.until(EC.element_to_be_clickable((By.XPATH, "//a[contains(@href, '/products')]")))
    products_link.click()
    
    search_input = wait.until(EC.presence_of_element_located((By.XPATH, "//input[@id='search_product']")))
    search_input.send_keys("shirt")
    
    search_button = driver.find_element(By.XPATH, "//button[@id='submit_search']")
    search_button.click()
    
    title_searched = wait.until(
        EC.presence_of_element_located((By.XPATH, "//h2[contains(@class, 'title') and contains(text(), 'Searched Products')]"))
    )
    
    products_found = driver.find_elements(By.XPATH, "//div[contains(@class, 'product-image-wrapper')]")
    
    print(f"\n[INFO] Sección activa: '{title_searched.text}'")
    print(f"[INFO] Elementos visuales de productos detectados: {len(products_found)}")
    
    assert title_searched.is_displayed(), "El título de resultados no está visible."
    assert len(products_found) > 0, "La búsqueda no arrojó ningún elemento en la interfaz."
    print("TEST DE EJECUCIÓN: PASSED - El flujo de búsqueda funciona correctamente.")

except Exception as e:
    print(f"TEST DE EJECUCIÓN: FAILED - Error durante la automatización: {e}")
    
finally:
    driver.quit()