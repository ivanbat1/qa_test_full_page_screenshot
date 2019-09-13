from Screenshot import Screenshot_Clipping
from selenium import webdriver
import time
from PIL import Image
from io import BytesIO


def full_screenshot(driver, save_path):
    # initiate value
    save_path = save_path + '.png' if save_path[-4::] != '.png' else save_path
    img_li = []  # to store image fragment
    offset = 0  # where to start

    # js to get height
    height = driver.execute_script('return Math.max('
                                   'document.documentElement.clientHeight, window.innerHeight);')
    # js to get the maximum scroll height
    # Ref--> https://stackoverflow.com/questions/17688595/finding-the-maximum-scroll-position-of-a-page
    max_window_height = driver.execute_script('return Math.max('
                                              'document.body.scrollHeight, '
                                              'document.body.offsetHeight, '
                                              'document.documentElement.clientHeight, '
                                              'document.documentElement.scrollHeight, '
                                              'document.documentElement.offsetHeight);')

    # looping from top to bottom, append to img list
    # Ref--> https://gist.github.com/fabtho/13e4a2e7cfbfde671b8fa81bbe9359fb
    while offset < max_window_height:
        # Scroll to height
        driver.execute_script(f'window.scrollTo(0, {offset});')
        img = Image.open(BytesIO((driver.get_screenshot_as_png())))
        img_li.append(img)
        offset += height

    # Stitch image into one
    # Set up the full screen frame
    box = (0, height - height * (max_window_height / height - max_window_height // height), img_li[-1].size[0], img_li[-1].size[1])
    img_li[-1] = img_li[-1].crop(box)
    img_frame_height = sum([img_frag.size[1] for img_frag in img_li])
    img_frame = Image.new('RGB', (img_li[0].size[0], img_frame_height))
    offset = 0
    for img_frag in img_li:
        img_frame.paste(img_frag, (0, offset))
        offset += img_frag.size[1]
    img_frame.save(save_path)


def go_to_page(url, ranger):
    driver.get(url)
    driver.execute_script(open("./F.js").read())
    time.sleep(1)
    full_screenshot(driver, 'new' + str(ranger) + '.png')


verbose = 1
driver = webdriver.Chrome('C:/Users/ITUA/Desktop/chromedriver/chromedriver.exe')
driver.get("http://medlife.saprit.co.uk/about-us/")
elems = driver.find_elements_by_xpath("//a[@href]")
href_list = list(set())
for elem in elems:
    if elem.get_attribute("href").startswith('http://'):
        href_list.append(elem.get_attribute("href"))
i = 0
while i != len(href_list):
    go_to_page(href_list[i], i)
    i += 1
