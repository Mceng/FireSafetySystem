#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2020/3/23 9:59
# @Author  : Mcen (mmocheng@163.com)
# @Name    : test_basicData_selectByPrimaryKey

import allure
from base import consts

CASEID = 2


@allure.feature('基础数据')
class Test_basicData():

    @allure.story('新建建筑')
    @allure.severity('critical')
    def test_basicData_addBuliting_pass(self, request_init, assert_init, params_init):
        """
        用例描述：新建建筑正向用例

        """
        self.params = params_init.get_params_list('test_basicData')
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