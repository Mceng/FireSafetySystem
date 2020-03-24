#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2020/3/17 16:08
# @Author  : Mcen (mmocheng@163.com)
# @Name    : test_basicData_getBuilding

import allure
from base import consts
import pytest
CASEID=2

@allure.feature('左侧列表')
class Test_BasicData():

    @allure.story('获取建筑信息列表')
    @allure.severity('critical')
    def test_getBuilding_pass(self,request_init,assert_init,params_init):

        """
        用例描述：获取获取建筑ID列表用例
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

    @allure.story('获取建筑信息列表')
    @allure.severity('critical')
    @pytest.mark.parametrize('buildingName,flag',[('建筑','true'),('建筑11111','true')])
    def test_getBuilding_s_pass(self,request_init,assert_init,params_init,buildingName,flag):

        """
        用例描述：获取获取建筑ID列表用例
        """
        self.params = params_init.get_params_list('test_content')

        datas = {
            "url": self.params['Info'][CASEID]['url'],
            "json": self.params['Info'][CASEID]['json'],
            "headers": self.params['Info'][CASEID]['header'],
            "method": self.params['Info'][CASEID]['method']
        }

        datas['json']['buildingName'] = buildingName
        datas['json']['flag'] = flag
        response = request_init.run_request(**datas)

        assert assert_init.assert_code(response['code'], 200)
        assert assert_init.assert_body(response['body'], 'msg', 'OK')
        assert assert_init.assert_time(response['time_consuming'], 1100)
        consts.RESULT_LIST.append('True')