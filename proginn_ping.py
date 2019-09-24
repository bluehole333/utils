# -*- coding: utf-8 -*-
"""
程序员客栈登录
"""

import requests
from selenium import webdriver
from bs4 import BeautifulSoup
import time

LOGIN_URL = 'https://www.proginn.com/'
PING_URL = 'https://www.proginn.com/wo/work_todo'

# 登录用户名和密码
USER_NMAE = ''
PASSWD = ''

# 自定义headers
HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.14; rv:69.0) Gecko/20100101 Firefox/69.0',
    'Referer': 'https://www.proginn.com/wo/work_todo',
    'Host': 'www.proginn.com',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
    'Connection': 'keep-alive'
}


class ProginnPing(object):
    def __init__(self, headers, user, passwd):
        '''
        类的初始化

        headers：请求头
        cookies: 持久化访问
        info_list: 存储账单信息的列表
        '''
        self.headers = headers
        # 初始化用户名和密码
        self.user = user
        self.passwd = passwd
        # 利用requests库构造持久化请求
        self.session = requests.Session()
        # 将请求头添加到缓存之中
        self.session.headers = self.headers
        # 初始化存储列表
        self.info_list = []

    def wait_input(self, ele, text):
        for item in text:
            ele.send_keys(item)
            time.sleep(0.5)

    def get_cookies(self):
        option = webdriver.Firefox()
        option.maximize_window()
        option.get(LOGIN_URL)
        option.implicitly_wait(3)

        # 1. 打开登录悬浮框
        links = option.find_element_by_xpath('//a[@class="item login ajax_login_btn"]')
        links.click()

        # 2. 激活手机号登录窗口
        option.find_element_by_id('J_ChangeWay').click()

        # 3. 输入用户名
        uname = option.find_element_by_xpath('//input[@placeholder="您的手机号"]')
        print('正在输入账号.....')
        self.wait_input(uname, self.user)
        time.sleep(1)

        # 4. 输入密码
        upass = option.find_element_by_id('password')
        print('正在输入密码....')
        self.wait_input(upass, self.passwd)
        time.sleep(1)

        # 5. 点击登录按钮
        butten = option.find_element_by_id('login_submit')
        time.sleep(1)
        butten.click()

        print('正在跳转页面....')
        option.get(PING_URL)
        print('当前页面:', option.current_url)
        option.implicitly_wait(3)

        # 8. ping
        option.find_element_by_xpath('//span[@data-position="bottom right"]').click()

        # option.save_screenshot('1.png')
        # 7. 保存cookie并转换为dict
        cookies = option.get_cookies()
        cookies_data = {}
        for cookie in cookies:
            if 'name' in cookie and 'value' in cookie:
                cookies_data[cookie['name']] = cookie['value']

        return cookies_data

    def set_cookies(self):
        """
        将获取到的cookies加入session
        """
        c = self.get_cookies()
        self.session.cookies.update(c)
        print(self.session.cookies)

    def login_status(self):
        """
        判断登录状态
        """
        self.set_cookies()
        status = self.session.get(PING_URL, timeout=5, allow_redirects=False).status_code
        print("登录状态:", status)
        if status == 200:
            return True
        else:
            return False

    def ping(self):
        status = self.login_status()
        # 登录成功 可以运行其他操作
        if status:
            pass


ProginnPing(HEADERS, USER_NMAE, PASSWD).ping()
