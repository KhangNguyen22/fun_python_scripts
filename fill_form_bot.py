from selenium import webdriver
from time import sleep
from faker import Faker
from sys import stdin
from random import randint

firefox_profile = webdriver.FirefoxProfile()
firefox_profile.set_preference("browser.privatebrowsing.autostart", True)

def bot(fname,lname,email_address):
    driver = webdriver.Firefox(firefox_profile=firefox_profile)
    driver.get("PUT_ADDRESS_HERE")
    first_name = driver.find_element_by_id('firstName')
    first_name.send_keys(fname)
    last_name = driver.find_element_by_id('lastName')
    last_name.send_keys(lname)
    email_id = driver.find_element_by_id('email') 
    email_id.send_keys(email_address)
    try:
        sleep(15)
        # email_id.submit()
        driver.delete_all_cookies()
        driver.close()
    except:
        print("Fail")
        driver.delete_all_cookies()
        driver.close()

try:
    file1 = open('names.txt','r')
    for _ in range(40):
        fake = Faker()
        e = fake.email()
        full_name=file1.readline().strip('\n').split(' ')
        first_name = full_name[0]
        last_name = full_name[1]
        bot(first_name,last_name,e)

except:
    print("Failed LOOOP")