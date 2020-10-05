from sel_functions import *
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys





    
''' LOGIN '''
chrome_driver = r"C:\Users\third\Downloads\chromedriver_win32\chromedriver"
browser = webdriver.Chrome(executable_path=chrome_driver)
browser.get("https://sso.godaddy.com/")
time.sleep(2)
browser.find_element_by_id("username").send_keys("*****USERNAME********")
browser.find_element_by_id("password").send_keys("*****PASSWORD********")
browser.find_element_by_id("submitBtn").click()
cookies = browser.get_cookies()
time.sleep(3)

id_list = iterate(20, browser)

for user in id_list:
    unsubscribe(user, browser, cookies)





