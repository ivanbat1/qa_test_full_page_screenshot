from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec

binary = "C:\Program Files (x86)\Google\Chrome\Application"
caps = DesiredCapabilities().CHROME
caps["pageLoadStrategy"] = "none"  # interactive
options = webdriver.ChromeOptions()
options.add_argument("--start-maximized")
driver = webdriver.Chrome('C:/Users/ITUA/Desktop/chromedriver/chromedriver.exe',
                          chrome_options=options,
                          desired_capabilities=caps)

driver.get("https://medlaif.com/uk/")
wait = WebDriverWait(driver, 10)
men_menu = wait.until(ec.visibility_of_element_located((By.ID, "menu")))
list_href = []
list_title = [i for i in driver.find_elements_by_css_selector('#menu a')]

list_href = list(set(list_href))
i = 0

while i < len(list_href):
    driver.get(list_href[i])
    wait = WebDriverWait(driver, 10)
    men_menu = wait.until(ec.visibility_of_element_located((By.ID, "menu")))
    title = driver.title
    list_title.append(title)
    i += 1
print(list_title)
