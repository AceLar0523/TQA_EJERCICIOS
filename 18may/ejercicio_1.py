from selenium import webdriver
from selenium.webdriver.common.by import By
import time

Usuario = "standard_user"

Password = "secret_sauce"

driver = webdriver.Chrome()

driver.get("https://www.saucedemo.com/")

driver.maximize_window()

user_name = driver.find_element(By.XPATH, '//input[@id="user-name"]')
user_name.click()
user_name.send_keys(Usuario)
time.sleep(5)
user_name.clear()

contrasena = driver.find_element(By.ID, "password")
contrasena.click()
contrasena.send_keys(Password)

boton_login = driver.find_element(By.XPATH, '//input[@data-test="login-button"]')
boton_login.click()

time.sleep(5)

driver.quit() #cuando se hago un monton de pruebas para que no guarde en el cache
