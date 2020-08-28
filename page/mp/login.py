#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2020/8/23 15:08
# @Author : zbl
# @Site : 
# @File : login.py
# @Software: PyCharm
import time

import allure
from selenium.webdriver.common.by import By

from base.web_base.base_page import BaseHandle, BaseProxy
from base.web_base.base_page import BaseElement


class LoginElement(BaseElement):
    def __init__(self):
        super().__init__()
        self.username = (By.CSS_SELECTOR, "[placeholder='请输入手机号']")
        self.code = (By.CSS_SELECTOR, '[placeholder="验证码"]')
        self.login_btn = (By.CSS_SELECTOR, '.el-button--primary')
        self.prompt = (By.CSS_SELECTOR, '.el-message')

    def find_username(self):
        return self.find_elt(self.username)

    def find_code(self):
        return self.find_elt(self.code)

    def find_login_btn(self):
        return self.find_elt(self.login_btn)

    def find_prompt(self):
        return self.find_elt(self.prompt)


class LoginHandle(BaseHandle):
    def __init__(self):
        self.loginElement = LoginElement()

    @allure.step(title="输入用户名")
    def send_username(self, username):
        self.input_text(self.loginElement.find_username(), username)

    @allure.step(title="输入验证码")
    def send_code(self, code):
        self.input_text(self.loginElement.find_code(), code)

    @allure.step(title="点击登陆")
    def click_login_btn(self):
        self.loginElement.find_login_btn().click()

    @allure.step(title="获取提示信息")
    def get_text_prompt(self):
        return self.get_text(self.loginElement.find_prompt())


class LoginProxy(BaseProxy):
    def __init__(self):
        self.loginHandle = LoginHandle()

    def login(self, username, code, check):
        """
        登陆方法
        :param username: 账号
        :type username: str
        :param code: 验证码
        :type code: str
        :param check:预期结果
        :return:
        :rtype:
        """
        self.loginHandle.send_username(username)
        self.loginHandle.send_code(code)
        self.loginHandle.click_login_btn()
        self.assert_in(check, self.loginHandle.get_text_prompt())
        time.sleep(5)
