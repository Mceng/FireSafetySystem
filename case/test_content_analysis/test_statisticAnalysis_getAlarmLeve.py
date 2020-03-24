#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2020/3/18 15:05
# @Author  : Mcen (mmocheng@163.com)
# @Name    : test_statisticAnalysis_getAlarmLeve

import allure
import pytest
from base import consts
from params.datas.test_content_analysis import D
CASEID = 4


@allure.feature('统计分析')
class Test_Analysis():

    @allure.story('告警次数排名表')
    @allure.severity('critical')
    @pytest.mark.parametrize('buildingId,flag',D.buildingId_flag())
    @pytest.mark.parametrize('dayCount',D.dayCount())
    def test_statisticAnalysis_getAlarmLeve_pass(self, request_init, assert_init, params_init,buildingId,flag,dayCount):
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
        datas['json']['flag'] = flag
        datas['json']['buildingId'] = buildingId
        datas['json']['dayCount'] = dayCount

        response = request_init.run_request(**datas)
        assert assert_init.assert_code(response['code'], 200)
        assert assert_init.assert_body(response['body'], 'msg', 'OK')
        assert assert_init.assert_time(response['time_consuming'], 1100)
        consts.RESULT_LIST.append('True')

    @allure.story('告警次数排名表')
    @allure.severity('critical')
    @pytest.mark.parametrize('dayCount,start,end', D.end_start())
    def test_statisticAnalysis_getAlarmLeve_s_pass(self, request_init, assert_init, params_init,dayCount,start,end):
        """
        用例描述：告警次数排名表通过搜索日期进行搜索统计

        """
        self.params = params_init.get_params_list('test_content_analysis')
        datas = {
            "url": self.params['MessageInfo'][CASEID]['url'],
            "json": self.params['MessageInfo'][CASEID]['json'],
            "headers": self.params['MessageInfo'][CASEID]['header'],
            "method": self.params['MessageInfo'][CASEID]['method']
        }
        datas['json']['dayCount'] = dayCount
        datas['json']['start'] = start
        datas['json']['end'] = end


        response = request_init.run_request(**datas)
        assert assert_init.assert_code(response['code'], 200)
        assert assert_init.assert_body(response['body'], 'msg', 'OK')
        assert assert_init.assert_time(response['time_consuming'], 1100)
        consts.RESULT_LIST.append('True')