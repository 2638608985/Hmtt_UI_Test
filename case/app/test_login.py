#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2020/8/23 16:35
# @Author : zbl
# @Site : 
# @File : test_login.py
# @Software: PyCharm
import pytest

from page.app.login import App_LoginProxy


class Test_App_Login:

    # @pytest.mark.run(1)
    # @pytest.mark.parametrize(("username", "code", "check"), Get_Data.get_data_json("login.json", direction=0))
    # def test_login(self, username, code, check):
    #     LoginProxy().login(username, code, check)

    @pytest.mark.run(order=1)
    def test_app_login(self, app_login):
        print("-------------1---------------------test_app_login-----------1---------------------")
        App_LoginProxy().app_login(*app_login)
