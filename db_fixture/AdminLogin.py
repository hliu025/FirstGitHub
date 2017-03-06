import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

import requests
def login(driver):
    driver.get("http://172.16.1.12/login")
    driver.find_element_by_id("mhtlogin").click()
    driver.find_element_by_name("username").send_keys("admin")
    driver.find_element_by_name("username").send_keys(Keys.TAB)
    driver.find_element_by_name("password").send_keys("8811870")
    driver.find_element_by_name("captcha").send_keys("pass")
    driver.find_element_by_id("loginbtn").click()
    driver.maximize_window()
    time.sleep(10)

