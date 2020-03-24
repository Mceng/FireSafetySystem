#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2020/3/18 14:19
# @Author  : Mcen (mmocheng@163.com)
# @Name    : test_statisticAnalysis_getProcessTimeConsuming


import allure
import pytest
from base import consts
from params.datas.test_content_analysis import D
CASEID = 2


@allure.feature('统计分析')
class Test_Analysis():

    @allure.story('告警处理耗时统计图')
    @allure.severity('critical')
    @pytest.mark.parametrize('dayCount',D.dayCount())
    @pytest.mark.parametrize('buildingId',D.buildingId())
    def test_getProcessTimeConsuming_pass(self, request_init, assert_init, params_init,dayCount,buildingId):
        """
        用例描述：告警处理耗时统计图通过不同的天数进行搜索统计

        """
        self.params = params_init.get_params_list('test_content_analysis')
        datas = {
            "url": self.params['MessageInfo'][CASEID]['url'],
            "json": self.params['MessageInfo'][CASEID]['json'],
            "headers": self.params['MessageInfo'][CASEID]['header'],
            "method": self.params['MessageInfo'][CASEID]['method']
        }
        datas['json']['dayCount'] = dayCount
        datas['json']['buildingId'] = buildingId

        response = request_init.run_request(**datas)
        assert assert_init.assert_code(response['code'], 200)
        assert assert_init.assert_body(response['body'], 'msg', 'OK')
        assert assert_init.assert_time(response['time_consuming'], 1100)
        consts.RESULT_LIST.append('True')


    @allure.story('告警处理耗时统计图')
    @allure.severity('critical')
    @pytest.mark.parametrize('dayCount,start,end', D.end_start())
    def test_getProcessTimeConsuming_data_s_pass(self, request_init, assert_init, params_init,dayCount,start,end):
        """
        用例描述：告警处理耗时统计图通过搜索日期进行搜索统计

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