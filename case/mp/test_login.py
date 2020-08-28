#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2020/8/23 16:35
# @Author : zbl
# @Site : 
# @File : test_login.py
# @Software: PyCharm
import pytest

from page.mp.login import LoginProxy

@pytest.mark.usefixtures("login_class")
class Test_Login:

    # @pytest.mark.run(1)
    # @pytest.mark.parametrize(("username", "code", "check"), Get_Data.get_data_json("login.json", direction=0))
    # def test_login(self, username, code, check):
    #     LoginProxy().login(username, code, check)

    @pytest.mark.run(1)
    def test_login(self, login):
        LoginProxy().login(*login)
