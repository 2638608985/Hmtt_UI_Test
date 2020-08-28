#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2020/8/23 10:53
# @Author : zbl
# @Site : 
# @File : config.py
# @Software: PyCharm
import inspect
import logging.handlers
import os
from logging import Logger

import colorlog


class log:
    logger: Logger = None

    @classmethod
    def create_log(cls):
        """
        设置log
        :return:
        :rtype:
        """
        # 获取log对象，如果带参则新建log对象
        cls.logger = logging.getLogger("test")
        # 设置输出log的水平：DEBUG INFO WARNING ERROR CRITICAL
        cls.logger.setLevel(level=logging.DEBUG)
        # 创建记录器 输出到控制台
        ls = logging.StreamHandler()
        # 创建记录器 输出到文件
        # lht = logging.handlers.TimedRotatingFileHandler(filename="./log/ll_test.log", when="M", interval=1,
        #                                                 backupCount=2)
        # 创建log格式化对象，输出格式
        # formatter = logging.Formatter(
        #     fmt="%(asctime)s %(levelname)s [%(name)s] [%(filename)s(%(funcName)s:%(lineno)s)] - %(message)s")
        log_colors_config = {
            'DEBUG': 'cyan',
            'INFO': 'green',
            'WARNING': 'yellow',
            'ERROR': 'red',
            'CRITICAL': 'red',
        }
        formatter = colorlog.ColoredFormatter(
            '%(log_color)s[%(asctime)s] [%(filename)s:%(lineno)d] '
            '[%(module)s:%(funcName)s] [%(levelname)s]- %(message)s',
            log_colors=log_colors_config)
        # 装载格式化对象
        ls.setFormatter(formatter)
        # lht.setFormatter(formatter)
        # 装载记录器
        cls.logger.addHandler(ls)
        # logger.addHandler(lht)
        # return logger

    @staticmethod
    def get_call_path(level: int = 0):
        """
        获取调用该方法的跟踪路径
        :param level: 0:当前方法开始，1：当前方法的上级方法开始
        :type level: int
        :return: 调用此方法的路径、方法、行数
        :rtype:
        """
        call_path = ""
        # 获取当前项目路径
        file_path = os.path.dirname(__file__)
        for i in range(level+1, len(inspect.stack())):
            if file_path in inspect.stack()[i][1]:
                call_path = call_path + "文件路径：" + inspect.stack()[i][1] + " 方法名：" + inspect.stack()[i][
                    3] + " 行数：" + str(
                    inspect.stack()[i][2]) + " <--\n"
            else:
                break
        return call_path
