from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec

driver = webdriver.Chrome('C:/Users/ITUA/Desktop/chromedriver/chromedriver.exe')

def login(drivr, login, pasw):
    driver.find_element_by_id('user_login').send_keys(login)
    driver.find_element_by_id('user_pass').send_keys(pasw)
    driver.find_element_by_id('wp-submit').click()

def got_to_make_page(dri0ver, text='.Наши специалисты'):
    driver.find_elements_by_xpath("//*[.wp-menu-name(text(), " + text + ")]").click()
    driver.find_element_by_class_name(".page-title-action").click()

def make(drive, ranger):
    driver.find_element_by_id('title').send_keys('Жуков Парамон Антонович ' + ranger)


