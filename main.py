import time

from contants import *
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get(APP_URL)
driver.maximize_window()
waitElement = WebDriverWait(driver, 20)
waitElement.until(EC.visibility_of_element_located((By.XPATH, PAY_NOW_BTN)))
driver.find_element(By.XPATH, PAY_NOW_BTN).click()
waitElement.until(EC.invisibility_of_element((By.CLASS_NAME, LOADING_SCREEN)))
waitElement.until(EC.presence_of_element_located((By.XPATH, SPLIT_BILL_BTN)))
waitElement.until(EC.visibility_of_element_located((By.XPATH, SPLIT_BILL_BTN)))
waitElement.until(EC.element_to_be_clickable((By.XPATH, SPLIT_BILL_BTN)))
elem = driver.find_element(By.XPATH, SPLIT_BILL_BTN)
driver.execute_script("arguments[0].click();", elem)
waitElement.until(EC.presence_of_element_located((By.ID, CUSTOM_AMNT_BTN)))
elem = driver.find_element(By.ID, CUSTOM_AMNT_BTN)
driver.execute_script("arguments[0].click();", elem)
waitElement.until(EC.visibility_of_element_located((By.ID, CUSTOM_AMNT_FIELD)))
driver.find_element(By.ID, CUSTOM_AMNT_FIELD).send_keys(SPLIT_AMNT)
driver.find_element(By.ID, CONFIRM_BTN).click()
elem = driver.find_element(By.ID, FIVE_TIP_BTN)
driver.execute_script("arguments[0].click();", elem)
waitElement.until(EC.visibility_of_element_located((By.ID, CARD_NUMBER_IFRAME)))
driver.switch_to.frame(CARD_NUMBER_IFRAME)
driver.find_element(By.ID, CARD_NUMBER_INPUT).send_keys(CARD_INFO)
driver.switch_to.default_content()
driver.switch_to.frame(EXPIRY_DATE_IFRAME)
driver.find_element(By.ID, EXPIRY_DATE_INPUT).send_keys(EXPIRY_DATE)
driver.switch_to.default_content()
driver.switch_to.frame(CVV_IFRAME)
driver.find_element(By.ID, CVV_INPUT).send_keys(CVV_INFO)
driver.switch_to.default_content()
driver.find_element(By.ID, CHECK_OUT_BTN).click()
waitElement.until(EC.presence_of_element_located((By.NAME, PAYMENT_IFRAME)))
driver.switch_to.frame(PAYMENT_IFRAME)
driver.find_element(By.ID, PASSWORD_INPUT).send_keys(PASSWORD_INFO)
driver.find_element(By.ID, CONTINUE_BUTTON).click()
driver.switch_to.default_content()
waitElement.until(EC.visibility_of_element_located((By.XPATH, SUCCESSFUL_PAYMENT)))
scpayment = driver.find_element(By.XPATH, SUCCESSFUL_PAYMENT).text
assert scpayment == "Payment was successful!", "Unsuccessful payment"