import selenium
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
import selenium.common.exceptions
import time
import re
from selenium.webdriver.support import expected_conditions as EC

store_check = time.time() + 5
service = Service()
options = webdriver.ChromeOptions()
driver = webdriver.Chrome(service=service, options=options)
driver.get("https://orteil.dashnet.org/cookieclicker/")


element = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID, "langSelect-EN")))
language = driver.find_element(By.ID, value='langSelect-EN')
language.click()
lement = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, "cc_banner")))
cc_button = driver.find_element(By.CLASS_NAME, value='cc_banner')
clicker = driver.find_element(By.ID, value='bigCookie')
element2 = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID, "bigCookie")))
'''cc_button = driver.find_element(By.CSS_SELECTOR, value='div div a')
try:
    cc_button.click()
except selenium.common.exceptions.StaleElementReferenceException:
    cc_button = driver.find_element(By.LINK_TEXT, value='div div a')
    cc_button.click()'''
while True:
    try:
        clicker.click()
    except selenium.common.exceptions.StaleElementReferenceException:
        clicker = driver.find_element(By.ID, value='bigCookie')
        clicker.click()
    time.sleep(.1)
    if time.time() > store_check:

        upgrades = driver.find_elements(By.CSS_SELECTOR, value='#upgrades .enabled')
        if len(upgrades) > 0:
            for i in upgrades:
                try:
                    i.click()
                except selenium.common.exceptions.StaleElementReferenceException:
                    pass
        else:
            autoclickers = driver.find_elements(By.CLASS_NAME, value='unlocked')
            autoclickers = [upgrade.text.split() for upgrade in autoclickers]
            if not autoclickers:
                continue
            else:
                cur_cookies = (driver.find_element(By.ID, value='cookies')).text.split()[0]
                if "," in cur_cookies:
                    cur_cookies = re.sub(",", "", cur_cookies)
                for purchase in autoclickers[::-1]:
                    if "," in purchase[1]:
                        purchase[1] = re.sub(",", "", purchase[1])
                    if int(purchase[1]) <= int(cur_cookies):
                        index = autoclickers.index(purchase)
                        click_upgrade = driver.find_element(By.ID, value=f'product{index}')
                        try:
                            click_upgrade.click()
                        except selenium.common.exceptions.ElementClickInterceptedException:
                            print("Please scroll down on right-hand side.")


