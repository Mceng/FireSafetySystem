#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2020/3/10
# @Author  : Mcen (mmocheng@163.com)
# @Name    : test_enterprise_getMonitoringMessageInfo

import allure
from base import consts
CASEID=1

@allure.feature('监控中心数据')
class Test_MapIndex():

    @allure.story('监控中心6种设备信息')
    @allure.severity('critical')
    def test_getMonitoringMessageInfo_pass(self,request_init,assert_init,params_init):

        """
        用例描述：监控中心6种设备信息正向用例
        """
        self.params = params_init.get_params_list('test_MonitoringSupervise')

        url = self.params['MessageInfo'][CASEID]['url']
        json = self.params['MessageInfo'][CASEID]['json']
        headers = self.params['MessageInfo'][CASEID]['header']
        method=self.params['MessageInfo'][CASEID]['method']

        response = request_init.run_request(method=method,url=url,data=None,json=json,headers=headers)

        assert assert_init.assert_code(response['code'], 200)
        assert assert_init.assert_body(response['body'], 'msg', 'OK')
        assert assert_init.assert_time(response['time_consuming'], 1100)
        consts.RESULT_LIST.append('True')