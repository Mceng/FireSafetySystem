#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2020/3/18 14:37
# @Author  : Mcen (mmocheng@163.com)
# @Name    : test_statisticAnalysis_getAlarmRatio


import allure
import pytest
from base import consts
from params.datas.test_content_analysis import D
CASEID = 3


@allure.feature('统计分析')
class Test_Analysis():

    @allure.story('告警环比统计图')
    @allure.severity('critical')
    @pytest.mark.parametrize('buildingId',D.buildingId())
    @pytest.mark.parametrize('year',D.year())
    def test_statisticAnalysis_getAlarmRatio_HBT_pass(self, request_init, assert_init, params_init,buildingId,year):
        """
        用例描述：告警处理耗时统计图-环比图通过不同的年份进行搜索统计

        """
        self.params = params_init.get_params_list('test_content_analysis')
        datas = {
            "url": self.params['MessageInfo'][CASEID]['url'],
            "json": self.params['MessageInfo'][CASEID]['json'],
            "headers": self.params['MessageInfo'][CASEID]['header'],
            "method": self.params['MessageInfo'][CASEID]['method']
        }
        datas['json']['year'] = year
        datas['json']['buildingId'] = buildingId
        datas['json']['remark'] = 0

        response = request_init.run_request(**datas)
        assert assert_init.assert_code(response['code'], 200)
        assert assert_init.assert_body(response['body'], 'msg', 'OK')
        assert assert_init.assert_time(response['time_consuming'], 1100)
        consts.RESULT_LIST.append('True')


    @allure.story('告警环比统计图')
    @allure.severity('critical')
    @pytest.mark.parametrize('buildingId',D.buildingId())
    @pytest.mark.parametrize('year',D.year())
    @pytest.mark.parametrize('month',D.month())
    def test_statisticAnalysis_getAlarmRatio_TBT_pass(self, request_init, assert_init, params_init,month,buildingId,year):
        """
        用例描述：告警处理耗时统计图-同比图通过不同的月份进行搜索统计

        """
        self.params = params_init.get_params_list('test_content_analysis')
        datas = {
            "url": self.params['MessageInfo'][CASEID]['url'],
            "json": self.params['MessageInfo'][CASEID]['json'],
            "headers": self.params['MessageInfo'][CASEID]['header'],
            "method": self.params['MessageInfo'][CASEID]['method']
        }
        datas['json']['year'] = year
        datas['json']['month'] = month
        datas['json']['buildingId'] = buildingId
        datas['json']['remark'] = 1

        response = request_init.run_request(**datas)
        assert assert_init.assert_code(response['code'], 200)
        assert assert_init.assert_body(response['body'], 'msg', 'OK')
        assert assert_init.assert_time(response['time_consuming'], 1100)
        consts.RESULT_LIST.append('True')