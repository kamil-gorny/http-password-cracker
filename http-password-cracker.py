from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import argparse

#webdriver configuration
PATH = "C:\Program Files (x86)\chromedriver.exe"
options = webdriver.ChromeOptions()
options.headless = True 
options.add_experimental_option("excludeSwitches", ["enable-logging"])
driver = webdriver.Chrome(options=options, executable_path=PATH)

class bgcolor:
    OKCYAN = '\033[96m'
    ENDC = '\033[0m'
def connect_to_website(driver, website):
    driver.get(website)

def display_logo():
    f = open('logo.txt', 'r')
    print(bgcolor.OKCYAN + f.read() + bgcolor.ENDC)
    print("""Usage:
    python http-password-cracker.py -L logins.txt -P passwords.txt """)
    print("""\nOptions:
    -u Set Url to crack password
    -l LOGIN or -L FILE login with LOGIN name or load list of logins 
    -p PASSWORD or -P FILE login with PASSWORD or load list of passwords
    -s Stop on matching credentials 
    -o Store credentials in the external file""")
display_logo()