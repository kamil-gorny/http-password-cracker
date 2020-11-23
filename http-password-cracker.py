from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import argparse
import time
from sys import argv
#webdriver configuration
options = webdriver.ChromeOptions()
    # options.headless = True 
PATH = "C:\Program Files (x86)\chromedriver.exe"
DRIVER = webdriver.Chrome(options=options, executable_path=PATH)
#python http-password-cracker.py host admin password admininput passwordinput 
script, host, admin, password, admininput, passwordinput = argv
class bgcolor:
    OKCYAN = '\033[96m'
    ENDC = '\033[0m'

def wait_to_find(input):
    try:
        WebDriverWait(DRIVER, 10).until(
            EC.element_to_be_clickable((By.NAME, input))
        )
    except:
        print("Not found")

def find_and_fill(input_data,input_field):
    wait_to_find(input_field)
    element = DRIVER.find_element_by_name(input_field)
    element.send_keys(input_data)

def submit_form():
    xpath = "//input[@type='submit']"
    try:
        WebDriverWait(DRIVER, 10).until(
            EC.element_to_be_clickable((By.XPATH, xpath))
        )
    except:
        print("Not found")
    
    element = DRIVER.find_element_by_xpath(xpath)
    element.send_keys(Keys.RETURN)

def connect_to_website(website):
    options.add_experimental_option("excludeSwitches", ["enable-logging"])
    DRIVER.get(website)
    
def display_logo():
    f = open('logo.txt', 'r')
    print(bgcolor.OKCYAN + f.read() + bgcolor.ENDC)
    
    print("""Usage:
    python http-password-cracker.py -L logins.txt -P passwords.txt """)
    print("""\nOptions:
    -v Verbose mode
    -u Set Url to crack password
    -l LOGIN or -L FILE login with LOGIN name or load list of logins 
    -p PASSWORD or -P FILE login with PASSWORD or load list of passwords
    -s Stop on matching credentials 
    -o Store credentials in the external file""")
display_logo()


def main():
    display_logo()
    connect_to_website(host)
    find_and_fill(admin, admininput)
    find_and_fill(password, passwordinput)
    submit_form()
    

if __name__ == "__main__":
    main()

