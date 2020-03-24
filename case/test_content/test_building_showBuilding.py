#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2020/3/17 16:08
# @Author  : Mcen (mmocheng@163.com)
# @Name    : test_building_showBuilding

import allure
from base import consts
import pytest
CASEID=3

@allure.feature('左侧列表')
class Test_BasicData():

    @allure.story('获取建筑信息')
    @allure.severity('critical')
    def test_showBuilding_pass(self,request_init,assert_init,params_init):

        """
        用例描述：获取建筑信息用例
        """
        self.params = params_init.get_params_list('test_content')
        datas = {
            "url": self.params['Info'][CASEID]['url'],
            "json": self.params['Info'][CASEID]['json'],
            "headers": self.params['Info'][CASEID]['header'],
            "method": self.params['Info'][CASEID]['method']
        }

        response = request_init.run_request(**datas)

        assert assert_init.assert_code(response['code'], 200)
        assert assert_init.assert_body(response['body'], 'msg', 'OK')
        assert assert_init.assert_time(response['time_consuming'], 1100)
        consts.RESULT_LIST.append('True')