from selenium import webdriver
from datetime import datetime
from framework.framework_qa import get_all_url_page, create_dir, go_to_page_make_screenshot, make_size

if __name__ == "__main__":
    url = "http://karniz.saprit.co.uk/"
    dict_size = {'1': '1280x720', '2': '992x744', '3': '768x1024', '4': '320x240'}
    driver = webdriver.Chrome('C:/Users/ITUA/Desktop/chromedriver/chromedriver.exe')
    driver.get(url)
    file_name = datetime.today().date()
    href_list = get_all_url_page(driver)
    i = 0
    print(href_list)
    print(len(dict_size))
    if len(dict_size) != 0:
        for phone, size in dict_size.items():
            file_path = '{}/{}'.format(file_name, size)
            create_dir(file_path)
            if size == 'max':
                driver.maximize_window()
            else:
                driver.set_window_size(*make_size(size))
            while i != len(href_list):
                go_to_page_make_screenshot(driver, href_list[i], i, file_path, "framework/F.js")
                i += 1
        driver.close()
    else:
        file_path = "{}".format(file_name)
        create_dir(file_path)
        driver.maximize_window()
        driver.implicitly_wait(10)
        go_to_page_make_screenshot(driver, href_list[i], i, file_path, "framework/F.js")
        driver.close()
