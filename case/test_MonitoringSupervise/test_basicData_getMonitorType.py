#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2020/3/17 10:47
# @Author  : Mcen (mmocheng@163.com)
# @Name    : test_basicData_getMonitorType


import allure
from base import consts
import pytest
from params.datas.test_MonitoringSupervise import D

CASEID = 4


@allure.feature('监控中心数据')
class Test_MapIndex():

    @allure.story('获取设备的卡片tab信息')
    @allure.severity('critical')
    def test_getMonitorType_pass(self, request_init, assert_init, params_init):
        """
        用例描述：通过点击左侧列表建筑获取设备的卡片tab信息正向用例

        """
        self.params = params_init.get_params_list('test_MonitoringSupervise')
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

    @allure.story('warningManger获取设备的卡片tab信息')
    @allure.severity('critical')
    @pytest.mark.parametrize("dealStatus,remark",D.warningManger_pass())
    def test_getMonitorType_warningManger_pass(self, request_init, assert_init, params_init,dealStatus,remark):
        """
        用例描述：告警处理\审核\综合查询界面下获取正向用例

        """
        self.params = params_init.get_params_list('test_MonitoringSupervise')
        datas = {
            "url": self.params['MessageInfo'][CASEID]['url'],
            "json": self.params['MessageInfo'][CASEID]['json'],
            "headers": self.params['MessageInfo'][CASEID]['header'],
            "method": self.params['MessageInfo'][CASEID]['method']
        }
        datas['json']['dealStatus']=dealStatus
        datas['json']['remark']=remark

        response = request_init.run_request(**datas)
        assert assert_init.assert_code(response['code'], 200)
        assert assert_init.assert_body(response['body'], 'msg', 'OK')
        assert assert_init.assert_time(response['time_consuming'], 1100)
        consts.RESULT_LIST.append('True')