#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2020/8/23 11:52
# @Author : zbl
# @Site : 
# @File : base_page.py
# @Software: PyCharm

# 对象库层-基类，把定位元素的方法定义在基类中
import time

from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait

from config import log
from utils.driverUtil import DriverUtil


# 1.定义对象库层的基类
class BaseElement:

    def __init__(self):
        # 获取浏览器驱动对象
        self.driver = DriverUtil.get_driver()

    # 公用的元素定位方法
    def find_elt(self, location):
        """
        公用定位元素方法 如果没找到会调用显示等待
        :param location: (By.XXX, "XXX")
        :type location:
        :return:
        :rtype:
        """
        try:
            time.sleep(0.3)
            return self.driver.find_element(*location)
        except Exception as e:
            # 可能是元素未加载出来，调用显示等待
            return self.find_elt_wait(location)

    def find_elt_wait(self, location, wait=10):
        """
        公用显示定位元素方法 默认等待10秒，一秒查询一次
        :param location: (By.XXX, "XXX")
        :type location:
        :param wait: 等待时长
        :type wait:
        :return:
        :rtype:
        """
        try:
            return WebDriverWait(self.driver, wait, 1).until(self.driver.find_element(*location))
        except Exception as e:
            if self.driver is not None:
                log.logger.debug("显示等待寻找元素出错{}{},\n跟踪路径:\n{}".format(*location, log.get_call_path()))
            else:
                log.logger.debug("浏览器对象不存在" + log.get_call_path())


# 1.定义操作层的基类
class BaseHandle:

    @staticmethod
    def select_by_index(element, index):
        Select(element).select_by_index(index)

    @staticmethod
    def select_by_value(element, value):
        Select(element).select_by_value(value)

    @staticmethod
    def select_by_visible_text(element, text):
        Select(element).select_by_visible_text(text)

    @staticmethod
    def get_text(element):
        """
        获取元素的文本内容
        :param element: 元素对象
        :type element:WebElement
        :return:
        :rtype:
        """
        if element is None or element == "":
            return None
        else:
            return element.text

    @staticmethod
    def input_text(element, text, sleep=0):
        """
        元素输入的方法，输入前会先清空
        :param element: 元素对象
        :type element:WebElement
        :param text: 输入的文本
        :type text: str
        :param sleep:
        :type sleep:
        :return:
        :rtype:
        """
        # 清空用户名输入框默认值
        element.clear()
        # 如果clear清空失败
        if element.get_attribute("value"):
            # 模拟点击删除按钮进行清空
            element.send_keys(chr(127) * len(element.get_attribute("value")))
        # 通过表示对象库层的实例属性来获取用户名输入框的元素对象,并执行输入
        element.send_keys(text)
        time.sleep(sleep)

    def select_by_type(self, element, pra, pra_type="text"):
        """
        pra_type:index、value、text,填错类型默认选择text
        :param element: 下拉框对象
        :type element:WebElement
        :param pra: 下拉框选择参数
        :type pra:
        :param pra_type: par类型
        :type pra_type: indxe、value、text
        :return:
        :rtype:
        """
        if pra_type == "index":
            self.select_by_index(element, pra)
        elif pra_type == "value":
            self.select_by_value(element, pra)
        else:
            self.select_by_visible_text(element, pra)


class BaseProxy:

    @staticmethod
    def assert_in(expected, actual):
        """
        断言actual包含expected
        :return:
        :rtype:
        """
        if actual == "" or actual is None and "成功" in expected:
            assert True, expected
            return
        if expected in actual:
            assert True, '"{}"中包含:"{}"'.format(actual, expected)
        else:
            assert False, '"{}"中不包含:"{}",\n调用路径：\n{}'.format(actual, expected, log.get_call_path())

    @staticmethod
    def assert_not_in(expected, actual):
        """
        断言actual不包含expected
        :return:
        :rtype:
        """
        if expected not in actual:
            assert True, '"{}"中不包含:"{}"'.format(actual, expected)
        else:
            assert False, '"{}"中包含:"{}"'.format(actual, expected)

    @staticmethod
    def assert_equal(expected, actual):
        """
        断言actual等于expected
        :param expected: 预期结果
        :param actual: 实际结果
        :return:
        :rtype:
        """
        if expected == actual:
            assert True, '"{}" 等于 "{}"'.format(actual, expected)
        else:
            assert False, '"{}" 不等于 "{}"'.format(actual, expected)

    @staticmethod
    def assert_not_equal(expected, actual):
        """
        断言actual不等于expected
        :param expected: 预期结果
        :param actual: 实际结果
        :return:
        :rtype:
        """
        if expected != actual:
            assert True, '"{}" 不等于 "{}"'.format(actual, expected)
        else:
            assert False, '"{}" 等于 "{}"'.format(actual, expected)

    @staticmethod
    def assert_big(expected, actual):
        """
        断言expected大于actual
        :param expected: 预期结果
        :param actual: 实际结果
        :return:
        :rtype:
        """
        if expected > actual:
            assert True, '"{}" 大于 "{}"'.format(expected, actual)
        else:
            assert False, '"{}" 不大于 "{}"'.format(expected, actual)

    @staticmethod
    def assert_big_or_equal(expected, actual):
        """
        断言expected>=actual
        :param expected: 预期结果
        :param actual: 实际结果
        :return:
        :rtype:
        """
        if expected >= actual:
            assert True, '"{}" 大于等于 "{}"'.format(expected, actual)
        else:
            assert False, '"{}" 小于 "{}"'.format(expected, actual)

    @staticmethod
    def assert_small(expected, actual):
        """
        断言expected小于actual
        :param expected: 预期结果
        :param actual: 实际结果
        :return:
        :rtype:
        """
        if expected < actual:
            assert True, '"{}" 小于 "{}"'.format(expected, actual)
        else:
            assert False, '"{}" 不小于 "{}"'.format(expected, actual)

    @staticmethod
    def assert_small_or_equal(expected, actual):
        """
        断言expected<=actual
        :param expected: 预期结果
        :param actual: 实际结果
        :return:
        :rtype:
        """
        if expected < actual:
            assert True, '"{}" 小于等于 "{}"'.format(expected, actual)
        else:
            assert False, '"{}" 大于 "{}"'.format(expected, actual)
