#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2020/8/19 13:13
# @Author : SuenDanny
# @Site : 
# @File : driverUtil.py
# @Software: PyCharm
import selenium.webdriver
import appium.webdriver

from config import log


class DriverUtil:
    __driver = None

    @classmethod
    def get_driver(cls):
        """获取浏览器对象"""
        # 判断__driver是否为空
        if cls.__driver is not None:
            return cls.__driver
        else:
            log.logger.debug("请先创建driver对象")

    @classmethod
    def quit_driver(cls):
        """
        关闭浏览器driver对象
        """
        if cls.__driver is not None:
            cls.__driver.quit()
            cls.__driver = None

    @classmethod
    def get_web_driver(cls, browser="Chrome", wait=10):
        """
        创建浏览器webdriver
        :param browser: 浏览器名称，默认Chrome
        :type browser: str
        :param wait:隐性等待时长/秒，默认等待10秒
        :type wait:int
        :return:
        :rtype:
        """
        if cls.__driver is None:
            if browser == "Chrome":
                cls.__driver = selenium.webdriver.Chrome()
            elif browser == "Firefox":
                cls.__driver = selenium.webdriver.Firefox()
            elif browser == "Remote":
                cls.__driver = selenium.webdriver.Remote()
            cls.__driver.maximize_window()
            cls.__driver.implicitly_wait(wait)
            # cls.__driver.find_element_by_link_text().text
        return cls.__driver

    # app系统获取驱动对象得方法
    @classmethod
    def get_app_driver(cls, platform_name="Android", platform_version="5.1", device_name="emulator-5554",
                       app_package="com.itcast.toutiaoApp", app_activity=".MainActivity",
                       url="http://localhost:4723/wd/hub"):
        """
        创建手机app的webdriver对象
        :param platform_name: 平台名称
        :type platform_name:
        :param platform_version: 平台版本
        :type platform_version:
        :param device_name: 设备名称
        :type device_name:
        :param app_package: app包名
        :type app_package:
        :param app_activity: app页面名
        :type app_activity:
        :param url:appium访问路径
        :type url:
        :return:
        :rtype:
        """
        if cls.__driver is None:
            desired_caps = dict()
            desired_caps['platformName'] = platform_name
            desired_caps['platformVersion'] = platform_version
            desired_caps['deviceName'] = device_name
            desired_caps['appPackage'] = app_package
            desired_caps['appActivity'] = app_activity
            cls.__driver = appium.webdriver.Remote(url, desired_caps)
        return cls.__driver

    @classmethod
    def find_elt_by_text(cls, text):
        """
        通过文本查询元素
        :param text:
        :type text:
        :return:
        :rtype:
        """
        try:
            return cls.__driver.find_element_by_link_text(text)
        except Exception as e:
            if cls.__driver is not None:
                log.logger.debug("该页面找不到文本信息为 {} 的元素".format(text))
            else:
                log.logger.debug("浏览器对象不存在")
            return None
