#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2020/3/10
# @Author  : Mcen (mmocheng@163.com)
# @Name    : superviseIndex_getCustomer


import allure
from base import consts


@allure.feature('大屏模块数据')
class Test_MapIndex():

    @allure.story('获取校企信息')
    @allure.severity('critical')
    def test_getCustomer_pass(self,request_init,assert_init,params_init):

        """
        用例描述：获取校企信息正向用例
        """
        self.params = params_init.get_params_list('mapIndex')

        url = self.params['MapIndex'][1]['url']
        json = self.params['MapIndex'][1]['json']
        headers = self.params['MapIndex'][1]['header']
        method=self.params['MapIndex'][1]['method']

        response = request_init.run_request(method=method,url=url,data=None,json=json,headers=headers)

        assert assert_init.assert_code(response['code'], 200)
        assert assert_init.assert_body(response['body'], 'msg', 'OK')
        assert assert_init.assert_time(response['time_consuming'], 1100)
        consts.RESULT_LIST.append('True')