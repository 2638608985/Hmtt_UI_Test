#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2020/8/23 21:51
# @Author : zbl
# @Site : 
# @File : get_data.py
# @Software: PyCharm
import json
import os

from utils.more_sql_Run import dbUtil


class Get_Data:
    __direction = 1

    @staticmethod
    def put_direction(direction: int = 1):
        __direction = direction

    @staticmethod
    def get_data_db(interface, direction=__direction):
        """
        查询符合要求的数据
        :param interface: 测试的接口
        :type interface: str
        :param direction: 测试方向：1正向、-1逆向、全部
        :type direction: int
        :return:
        :rtype:
        """
        # 查询接口名称为interface测试方向为direction的测试数据
        sql = "select "
        # 执行sql语句
        return dbUtil.run_sql()

    @staticmethod
    def get_data_json(file_name, direction=__direction):
        """
        通过文件名称获取json数据
        :param file_name: 文件名称
        :type file_name: str
        :param direction: 测试方向：1正向、-1逆向、全部
        :type direction: int
        :return:
        :rtype:
        """
        # 获取当前文件目录名
        path = os.path.dirname(__file__)
        # 拼接要读取的json文件路径
        json_path = path + "\\json_data\\" + file_name
        with open(json_path, encoding="utf-8") as f:
            json_data = json.load(f)
            # for data in json_data:
            # data_list = []
            test_data = []
            if direction == 1:
                data_list = json_data.get("positive")
            elif direction == -1:
                data_list = json_data.get("reverse")
            else:
                data_list = json_data.get("reverse")
                data_list = data_list + json_data.get("positive")
            for data_dict in data_list:
                for data in data_dict.values():
                    test_data.append(list(data.values()))
            return test_data
