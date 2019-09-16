from selenium import webdriver
from datetime import datetime
from framework.framework_qa import get_all_url_page, create_dir, go_to_page_make_screenshot, make_size


if __name__ == "__main__":
    list_size = ['360x667']
    driver = webdriver.Chrome('C:/Users/ITUA/Desktop/chromedriver/chromedriver.exe')
    driver.get("http://medlife.saprit.co.uk/about-us/")
    file_name = datetime.today().date()
    href_list = get_all_url_page(driver)
    i = 0
    for size in list_size:
        file_path = '{}/{}'.format(file_name, size)
        create_dir(file_path)
        driver.set_window_size(*make_size(size))
        while i != len(href_list):
            go_to_page_make_screenshot(driver, href_list[i], i, file_path, "framework/F.js")
            i += 1
