#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2020/8/23 11:10
# @Author : zbl
# @Site : 
# @File : conftest.py
# @Software: PyCharm
import pytest

from config import log
from data.get_data import Get_Data
from utils.driverUtil import DriverUtil


# driver = None
@pytest.fixture(scope="session", autouse=True)
def driver():
    """所有用例执行前、后执行"""
    log.create_log()
    # driver = DriverUtil.get_web_driver(wait=0)
    driver = DriverUtil.get_app_driver()
    yield driver
    DriverUtil.quit_driver()

@pytest.fixture(scope="class")
def login_class(driver):
    """登陆测试_类"""
    driver.get("http://ttmp.research.itcast.cn/#/login")

@pytest.fixture(scope="function", params=Get_Data.get_data_json("login.json", direction=0))
def login(request):
    """登陆测试_方法"""
    yield request.param

@pytest.fixture(scope="function", params=Get_Data.get_data_json("app_login.json", direction=1))
def app_login(request):
    """登陆测试_方法"""
    yield request.param



