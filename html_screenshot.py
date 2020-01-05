from selenium import webdriver


def simple_web_screenshot(url, save_name):
    browser = webdriver.Firefox()
    browser.get(url)
    browser.save_screenshot(save_name)
    browser.quit()


def full_web_screenshot(url, save_name):
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
            driver.execute_script(js_move)
            height = driver.execute_script(js_height)
            k += 1
        else:
            break

    scroll_width = driver.execute_script('return document.body.parentNode.scrollWidth')
    scroll_height = driver.execute_script('return document.body.parentNode.scrollHeight')
    print(scroll_width, scroll_height)
    driver.set_window_size(scroll_width, scroll_height)
    driver.get_screenshot_as_file(save_name)
    driver.quit()


if __name__ == '__main__':
    # 默认窗口截图
    simple_web_screenshot('https://baidu.com', 'simple_badiu.png')

    # 截取网页完整（长图）图片
    full_web_screenshot('https://baidu.com', 'full_badiu.png')
