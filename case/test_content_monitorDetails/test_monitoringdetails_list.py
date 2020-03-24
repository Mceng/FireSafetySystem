#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2020/3/17 11:19
# @Author  : Mcen (mmocheng@163.com)
# @Name    : test_monitoringdetails_list

import allure
from base import consts

CASEID = 0


@allure.feature('监控中心数据')
class Test_MapIndex():

    @allure.story('获取某个建筑详情信息')
    @allure.severity('critical')
    def test_monitoringdetails_list_pass(self, request_init, assert_init, params_init):
        """
        用例描述：监控详情获取某个建筑详情信息正向用例

        """
        self.params = params_init.get_params_list('test_content_monitorDetails')

        datas = {
            "url": self.params['MessageInfo'][CASEID]['url'],
            "json": self.params['MessageInfo'][CASEID]['json'],
            "headers": self.params['MessageInfo'][CASEID]['header'],
            "method": self.params['MessageInfo'][CASEID]['method']
        }

        response = request_init.run_request(**datas)

        assert assert_init.assert_code(response['code'], 200)
        assert assert_init.assert_body(response['body'], 'msg', 'OK')
        assert assert_init.assert_time(response['time_consuming'], 1100)
        consts.RESULT_LIST.append('True')