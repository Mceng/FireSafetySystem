#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2020/3/17 11:30
# @Author  : Mcen (mmocheng@163.com)
# @Name    : test_monitoringdetails_bigDatelist

import allure
import pytest
from base import consts
from params.datas.test_content_monitorDetails import D

print(D.bigDate_pass())

CASEID = 1


@allure.feature('监控中心数据')
class Test_MapIndex():

    @allure.story('获取获取监测趋势')
    @allure.severity('critical')
    @pytest.mark.parametrize("showTime,start,end",D.bigDate_pass())
    def test_monitoringdetails_bigDatelist_pass(self, request_init, assert_init, params_init,showTime,start,end):
        """
        用例描述：监控详情获取监测趋势正向用例

        """
        self.params = params_init.get_params_list('test_content_monitorDetails')

        datas = {
            "url": self.params['MessageInfo'][CASEID]['url'],
            "json": self.params['MessageInfo'][CASEID]['json'],
            "headers": self.params['MessageInfo'][CASEID]['header'],
            "method": self.params['MessageInfo'][CASEID]['method']
        }
        datas["json"]["showTime"] = showTime
        datas["json"]["start"] = start
        datas["json"]["end"] = end

        response = request_init.run_request(**datas)

        assert assert_init.assert_code(response['code'], 200)
        assert assert_init.assert_body(response['body'], 'msg', 'OK')
        assert assert_init.assert_time(response['time_consuming'], 1100)
        consts.RESULT_LIST.append('True')

