#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2020/3/23 11:24
# @Author  : Mcen (mmocheng@163.com)
# @Name    : test_checkDeviceList

import allure
from base import consts
import pytest
from params.datas.test_basicData import devicetypeid
CASEID = 3


@allure.feature('基础数据')
class Test_basicData():

    @allure.story('设备绑定信息')
    @allure.severity('critical')
    @pytest.mark.parametrize('devicetypeid',devicetypeid())
    def test_checkDeviceList_pass(self, request_init, assert_init, params_init,devicetypeid):
        """
        用例描述：设备绑定信息正向用例

        """
        self.params = params_init.get_params_list('test_basicData')
        datas = {
            "url": self.params['MessageInfo'][CASEID]['url'],
            "json": self.params['MessageInfo'][CASEID]['json'],
            "headers": self.params['MessageInfo'][CASEID]['header'],
            "method": self.params['MessageInfo'][CASEID]['method']
        }
        datas['json']['devicetypeid'] = devicetypeid



        response = request_init.run_request(**datas)
        assert assert_init.assert_code(response['code'], 200)
        assert assert_init.assert_body(response['body'], 'msg', 'OK')
        assert assert_init.assert_time(response['time_consuming'], 1100)
        consts.RESULT_LIST.append('True')