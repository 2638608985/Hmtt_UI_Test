#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2020/8/27 19:11
# @Author : zbl
# @Site : 
# @File : home.py
# @Software: PyCharm
import time

import allure
from selenium.webdriver.common.by import By

from base.app_base.base_page import BaseHandle, BaseProxy
from base.app_base.base_page import BaseElement


class HomeElement(BaseElement):
    def __init__(self):
        super().__init__()
        self.channel = (By.CLASS_NAME, "android.widget.HorizontalScrollView")
        """滚动区域"""

    def find_channel(self):
        return self.find_elt(self.channel)


class HomeHandle(BaseHandle):
    def __init__(self):
        self.homeElement = HomeElement()

    @allure.step(title="滑动滚动区域")
    def slide_channel(self):
        self.slide_element(self.homeElement.find_channel(), "left", "2000")

    @allure.step(title="点击频道")
    def click_channel(self, location):
        self.homeElement.find_elt(location)


class HomeProxy(BaseProxy):
    def __init__(self):
        self.homeHandle = HomeHandle()

    def select_channel(self, location):
        """
        选择频道
        :param location: 选择方式和频道名字(By.XXX, "XXX")
        :type location:
        :return:
        :rtype:
        """
        # 获取频道滚动区域元素
        channel_elt = self.homeHandle.homeElement.find_channel()
        self.find_elt_by_channel(channel_elt, location, "left")
