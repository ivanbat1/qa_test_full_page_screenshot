from selenium import webdriver
from datetime import datetime
from framework.framework_qa import get_all_url_page, create_dir, go_to_page_make_screenshot

if __name__ == "__main__":
    driver = webdriver.Chrome('C:/Users/ITUA/Desktop/chromedriver/chromedriver.exe')
    driver.get("http://medlife.saprit.co.uk/about-us/")
    file_name = datetime.today().date()
    create_dir(file_name)
    href_list = get_all_url_page(driver)
    i = 0
    while i != len(href_list):
        go_to_page_make_screenshot(driver, href_list[i], i, file_name, "framework/F.js")
        i += 1
