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

from base.app_base.base_page import BaseHandle, BaseProxy
from base.app_base.base_page import BaseElement


class App_LoginElement(BaseElement):
    def __init__(self):
        super().__init__()
        self.input = (By.CLASS_NAME, "android.widget.EditText")
        self.login_btn = (By.CLASS_NAME, "android.widget.Button")

    def find_username(self):
        return self.finds_elt(self.input)[0]

    def find_code(self):
        return self.finds_elt(self.input)[1]

    def find_login_btn(self):
        return self.find_elt(self.login_btn)


class App_LoginHandle(BaseHandle):
    def __init__(self):
        self.app_LoginElement = App_LoginElement()

    @allure.step(title="输入手机号")
    def send_username(self, username):
        self.input_text(self.app_LoginElement.find_username(), username)

    @allure.step(title="输入验证码")
    def send_code(self, code):
        self.input_text(self.app_LoginElement.find_code(), code)

    @allure.step(title="点击登陆")
    def click_login_btn(self):
        self.app_LoginElement.find_login_btn().click()


class App_LoginProxy(BaseProxy):
    def __init__(self):
        self.app_LoginHandle = App_LoginHandle()

    def app_login(self, username, code, check):
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
        time.sleep(5)
        self.app_LoginHandle.send_username(username)
        self.app_LoginHandle.send_code(code)
        self.app_LoginHandle.click_login_btn()
        time.sleep(5)
