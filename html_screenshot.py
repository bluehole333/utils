from selenium import webdriver
import time
import os.path


def webshot(url, save_name):
    options = webdriver.FirefoxOptions()
    options.add_argument('--headless')
    options.add_argument('--disable-gpu')
    driver = webdriver.Firefox(options=options)
    driver.maximize_window()
    # 返回网页的高度的js代码
    js_height = "return document.body.clientHeight"

    driver.get(url)
    k = 1
    height = driver.execute_script(js_height)
    while True:
        if k * 500 < height:
            js_move = "window.scrollTo(0,{})".format(k * 500)
            print(js_move)
            driver.execute_script(js_move)
            time.sleep(0.2)
            height = driver.execute_script(js_height)
            k += 1
        else:
            break
    scroll_width = driver.execute_script('return document.body.parentNode.scrollWidth')
    scroll_height = driver.execute_script('return document.body.parentNode.scrollHeight')
    driver.set_window_size(scroll_width, scroll_height)
    driver.get_screenshot_as_file(save_name)
    print("Process {} get one pic !!!".format(os.getpid()))
    time.sleep(0.1)


if __name__ == '__main__':
    webshot('https://baidu.com', 'badiu.png')
