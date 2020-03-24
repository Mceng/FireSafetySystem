#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2020/3/17 11:30
# @Author  : Mcen (mmocheng@163.com)
# @Name    : test_monitoringdetails_dataDetailslist

import allure
import pytest
from base import consts

CASEID = 1


@allure.feature('监控中心数据')
class Test_MapIndex():

    @allure.story('获取监测数据')
    @allure.severity('critical')
    def test_monitoringdetails_dataDetailslist_pass(self, request_init, assert_init, params_init):
        """
        用例描述：监控详情获取获取监测数据正向用例

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

    @allure.story('获取监测数据')
    @allure.severity('critical')
    @pytest.mark.parametrize("deviceStatusS",["0","0,1","1"])#设备状态
    @pytest.mark.parametrize("runStatusS",["0","0,1","1"])#监测状态
    @pytest.mark.parametrize("isAlarmBatteryS",["0","0,1","1"])#电压
    @pytest.mark.parametrize("showTime,start,end",
            [("customize","2020-03-03","2020-03-18"),
             ("now","","")])#时间搜索
    def test_monitoringdetails_dataDetailslist_s_pass(self, request_init, assert_init, params_init, \
                                                      deviceStatusS,runStatusS,isAlarmBatteryS,showTime,start,end):
        """
        用例描述：监控详情搜索获取监测数据

        """
        self.params = params_init.get_params_list('test_content_monitorDetails')

        datas = {
            "url": self.params['MessageInfo'][CASEID]['url'],
            "json": self.params['MessageInfo'][CASEID]['json'],
            "headers": self.params['MessageInfo'][CASEID]['header'],
            "method": self.params['MessageInfo'][CASEID]['method']
        }
        datas["json"]["deviceStatusS"] = deviceStatusS
        datas["json"]["runStatusS"] = runStatusS
        datas["json"]["isAlarmBatteryS"] = isAlarmBatteryS
        datas["json"]["showTime"] = showTime
        datas["json"]["start"] = start
        datas["json"]["end"] = end

        response = request_init.run_request(**datas)

        assert assert_init.assert_code(response['code'], 200)
        assert assert_init.assert_body(response['body'], 'msg', 'OK')
        assert assert_init.assert_time(response['time_consuming'], 1100)
        consts.RESULT_LIST.append('True')