#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2020/3/18 10:27
# @Author  : Mcen (mmocheng@163.com)
# @Name    : test_alarmManager_getAlarmMessage
import allure
import pytest
from base import consts
from params.datas.test_content_warningManger import D
CASEID = 1


@allure.feature('告警管理')
class Test_AlarmManager():

    @allure.story('获取监测点告警详情告警数据')
    @allure.severity('critical')
    @pytest.mark.parametrize('type',D.get_type())
    @pytest.mark.parametrize('dealType',D.get_Alarm_dealType())
    def test_alarmManager_getAlarmMessage_pass(self, request_init, assert_init, params_init,type,dealType):
        """
        用例描述：获取监测点告警详情告警数据正向用例

        """
        self.params = params_init.get_params_list('test_content_warningManger')
        datas = {
            "url": self.params['MessageInfo'][CASEID]['url'],
            "json": self.params['MessageInfo'][CASEID]['json'],
            "headers": self.params['MessageInfo'][CASEID]['header'],
            "method": self.params['MessageInfo'][CASEID]['method']
        }
        datas['json']['type'] = type
        datas['json']['dealType'] = dealType

        response = request_init.run_request(**datas)
        assert assert_init.assert_code(response['code'], 200)
        assert assert_init.assert_body(response['body'], 'msg', 'OK')
        assert assert_init.assert_time(response['time_consuming'], 1100)
        consts.RESULT_LIST.append('True')