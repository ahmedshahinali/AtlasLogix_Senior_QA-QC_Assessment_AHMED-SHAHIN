import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
#import pytest
driver = webdriver.Chrome()

class Test(unittest.TestCase):

    def test_1(assessment):
       
        url = "https://assessment.nexus-grid.ai/qa/"
        driver.get(url)
        driver.maximize_window()
        actions = ActionChains(driver)
        time.sleep(1)
        driver.find_element(By.CSS_SELECTOR, 'input[type="email"]').send_keys("admin.ahmed-shahin@atlaslogix.test")
        driver.find_element(By.CSS_SELECTOR, 'input[type="password"]').send_keys("Ikqo5KB6Ax9n_A0a")
        WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, 'button.button--primary'))
        ).click()
        time.sleep(1)
        dropdown = Select(driver.find_element(By.TAG_NAME, "select"))
        dropdown.select_by_index(1)
        WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, '//button[contains(text(), "Shipments")]'))
        ).click()
        time.sleep(1)
        driver.find_element(By.CSS_SELECTOR, 'input[placeholder="Search shipments"]').send_keys("NODATA")

        WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, 'button.row-action'))
        ).click()
        WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, '//button[@role="tab" and text()="Compliance"]'))
        ).click()
        WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, '//button[contains(text(), "Approve compliance")]'))
        ).click()
        time.sleep(1)
        driver.quit() 
    
assessment = Test()
assessment.test_1()



    
     
