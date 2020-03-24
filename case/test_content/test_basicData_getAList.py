#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2020/3/10
# @Author  : Mcen (mmocheng@163.com)
# @Name    : test_basicData_getAList

import allure
from base import consts
CASEID=0

@allure.feature('左侧列表')
class Test_MapIndex():

    @allure.story('获取建筑列表')
    @allure.severity('critical')
    def test_gbasicData_getAList_pass(self,request_init,assert_init,params_init):

        """
        用例描述：获取建筑列表正向用例
        """
        self.params = params_init.get_params_list('test_content')

        url = self.params['Info'][CASEID]['url']
        json = self.params['Info'][CASEID]['json']
        headers = self.params['Info'][CASEID]['header']
        method=self.params['Info'][CASEID]['method']

        response = request_init.run_request(method=method,url=url,data=None,json=json,headers=headers)

        assert assert_init.assert_code(response['code'], 200)
        assert assert_init.assert_body(response['body'], 'msg', 'OK')
        assert assert_init.assert_time(response['time_consuming'], 1100)
        consts.RESULT_LIST.append('True')