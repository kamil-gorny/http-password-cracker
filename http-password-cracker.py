from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import argparse

#webdriver configuration
PATH = "C:\Program Files (x86)\chromedriver.exe"
options = webdriver.ChromeOptions()
# options.headless = True 
options.add_experimental_option("excludeSwitches", ["enable-logging"])
driver = webdriver.Chrome(options=options, executable_path=PATH)

def connect_to_website(driver, website):
    driver.get(website)

