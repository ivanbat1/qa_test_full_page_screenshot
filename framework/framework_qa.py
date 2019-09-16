import os
from PIL import Image
from io import BytesIO

verbose = 1


def full_screenshot(driver, save_path, file_name):
    save_path = save_path + '.png' if save_path[-4::] != '.png' else save_path
    img_li = []  # to store image fragment
    offset = 0  # where to start
    # js to get height
    height = driver.execute_script('return Math.max('
                                   'document.documentElement.clientHeight, window.innerHeight);')
    # js to get the maximum scroll height
    max_window_height = driver.execute_script('return Math.max('
                                              'document.body.scrollHeight, '
                                              'document.body.offsetHeight, '
                                              'document.documentElement.clientHeight, '
                                              'document.documentElement.scrollHeight, '
                                              'document.documentElement.offsetHeight);')

    # looping from top to bottom, append to img list
    while offset < max_window_height:
        # Scroll to height
        driver.execute_script(f'window.scrollTo(0, {offset});')
        img = Image.open(BytesIO((driver.get_screenshot_as_png())))
        img_li.append(img)
        offset += height
    # Stitch image into one
    # Set up the full screen frame
    box = (0, height - height * (max_window_height / height - max_window_height // height), img_li[-1].size[0],
           img_li[-1].size[1])
    img_li[-1] = img_li[-1].crop(box)
    img_frame_height = sum([img_frag.size[1] for img_frag in img_li])
    img_frame = Image.new('RGB', (img_li[0].size[0], img_frame_height))
    offset = 0
    for img_frag in img_li:
        img_frame.paste(img_frag, (0, offset))
        offset += img_frag.size[1]
    img_frame.save('{}'.format(file_name) + '/' + save_path)


def get_all_url_page(driver):
    href_list = list()
    elems = driver.find_elements_by_xpath("//a[@href]")
    for elem in elems:
        if elem.get_attribute("href").startswith('http://'):
            href_list.append(elem.get_attribute("href"))
    return list(set(href_list))


def go_to_page_make_screenshot(driver, url, ranger, file_name, js_file):
    driver.get(url)
    driver.execute_script(open(js_file).read())
    full_screenshot(driver, 'new' + str(ranger) + '.png', file_name)


def create_dir(file_name):
    try:
        os.makedirs('{}'.format(file_name))
    except FileExistsError:
        print('file exist')


def make_size(string):
    size = string.split('x')
    return (size[0], size[1])

