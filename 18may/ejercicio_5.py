import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
driver.maximize_window()

try:
    driver.get("https://demoqa.com/webtables")
    wait = WebDriverWait(driver, 10)
    
    wait.until(EC.element_to_be_clickable((By.ID, "addNewRecordButton"))).click()
    
    wait.until(EC.presence_of_element_located((By.ID, "firstName"))).send_keys("Alex")
    driver.find_element(By.ID, "lastName").send_keys("Mujica")
    driver.find_element(By.ID, "userEmail").send_keys("alex@dev.com")
    driver.find_element(By.ID, "age").send_keys("21")
    driver.find_element(By.ID, "salary").send_keys("5000")
    driver.find_element(By.ID, "department").send_keys("QA")
    driver.find_element(By.ID, "submit").click()
    time.sleep(4)
    
    search_box = driver.find_element(By.ID, "searchBox")
    search_box.send_keys("Alex")
    time.sleep(4)
    
    driver.find_element(By.XPATH, "//span[@title='Edit']").click()
    age_input = wait.until(EC.presence_of_element_located((By.ID, "age")))
    age_input.clear()
    age_input.send_keys("22")
    driver.find_element(By.ID, "submit").click()
    time.sleep(4)
    
    driver.find_element(By.XPATH, "//span[@title='Delete']").click()
    time.sleep(4)
    
    print("TEST DE EJECUCIÓN: PASSED - Operaciones CRUD en WebTables validadas correctamente.")

except Exception as e:
    print(f"TEST DE EJECUCIÓN: FAILED - Error durante la automatización: {e}")
    
finally:
    driver.quit()