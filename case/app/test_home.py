#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2020/8/27 23:07
# @Author : zbl
# @Site : 
# @File : test_home.py
# @Software: PyCharm
import pytest
from selenium.webdriver.common.by import By

from page.app.home import HomeProxy


class Test_Home:
    @pytest.mark.run(order=2)
    def test_select_channel(self):
        print("--------------order_v1.1.1--push------------")
        location = (By.XPATH, "//*[contains(@text,'js')]")
        HomeProxy().select_channel(location)
