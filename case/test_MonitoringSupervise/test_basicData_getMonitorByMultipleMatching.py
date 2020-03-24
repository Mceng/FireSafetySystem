#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2020/3/17 10:48
# @Author  : Mcen (mmocheng@163.com)
# @Name    : test_basicData_getMonitorByMultipleMatching



import allure
import pytest
from base import consts
from params.datas.test_MonitoringSupervise import D

CASEID = 5


@allure.feature('监控中心数据')
class Test_MapIndex():
    @pytest.mark.skip('数据量太大，先不执行')
    @allure.story('获取设备的卡片信息以及头部的建筑信息')
    @allure.severity('critical')
    @pytest.mark.parametrize('connectStatus',D.connectStatus_runStatus_deviceStatus_enabled())
    @pytest.mark.parametrize('runStatus',D.connectStatus_runStatus_deviceStatus_enabled())
    @pytest.mark.parametrize('deviceStatus',D.connectStatus_runStatus_deviceStatus_enabled())
    @pytest.mark.parametrize('enabled',D.connectStatus_runStatus_deviceStatus_enabled())
    @pytest.mark.parametrize('target',D.target())
    @pytest.mark.parametrize('searchName',D.searchName())
    @pytest.mark.parametrize('type',D.type())
    def test_getMonitorByMultipleMatching_pass(self, request_init, assert_init, params_init, \
                               connectStatus,runStatus,deviceStatus,enabled,target,type,searchName):
        """
        用例描述：监控中心和监测点管理下获取设备的卡片信息以及头部的建筑信息正向用例

        """
        self.params = params_init.get_params_list('test_MonitoringSupervise')
        datas = {
            "url": self.params['MessageInfo'][CASEID]['url'],
            "json": self.params['MessageInfo'][CASEID]['json'],
            "headers": self.params['MessageInfo'][CASEID]['header'],
            "method": self.params['MessageInfo'][CASEID]['method']
        }
        datas['json']['connectStatus']=connectStatus
        datas['json']['runStatus']=runStatus
        datas['json']['deviceStatus']=deviceStatus
        datas['json']['enabled']=enabled
        datas['json']['target']=target
        datas['json']['type']=type
        datas['json']['searchName']=searchName

        response = request_init.run_request(**datas)
        assert assert_init.assert_code(response['code'], 200)
        assert assert_init.assert_body(response['body'], 'msg', 'OK')
        assert assert_init.assert_time(response['time_consuming'], 1100)
        consts.RESULT_LIST.append('True')

    @pytest.mark.skip('数据量太大，先不执行')
    @allure.story('获取设备的卡片信息以及头部的建筑信息')
    @allure.severity('critical')
    @pytest.mark.parametrize('connectStatus',D.connectStatus_runStatus_deviceStatus_enabled())
    @pytest.mark.parametrize('runStatus',D.connectStatus_runStatus_deviceStatus_enabled())
    @pytest.mark.parametrize('deviceStatus',D.connectStatus_runStatus_deviceStatus_enabled())
    @pytest.mark.parametrize('enabled',D.connectStatus_runStatus_deviceStatus_enabled())
    @pytest.mark.parametrize('searchName',D.searchName())
    @pytest.mark.parametrize('type',D.type())
    @pytest.mark.parametrize('deal_status',D.deal_status())
    def test_getMonitorByMultipleMatching_s_pass(self, request_init, assert_init, params_init,\
                               connectStatus,runStatus,deviceStatus,enabled,type,searchName,deal_status):
        """
        用例描述：告警管理模块通过搜索获取设备的卡片信息正向用例

        """
        self.params = params_init.get_params_list('test_MonitoringSupervise')
        datas = {
            "url": self.params['MessageInfo'][CASEID]['url'],
            "json": self.params['MessageInfo'][CASEID]['json'],
            "headers": self.params['MessageInfo'][CASEID]['header'],
            "method": self.params['MessageInfo'][CASEID]['method']
        }
        datas['json']['connectStatus']=connectStatus
        datas['json']['runStatus']=runStatus
        datas['json']['deviceStatus']=deviceStatus
        datas['json']['enabled']=enabled
        datas['json']['target']="2"
        datas['json']['flag']="true"
        datas['json']['type']=type
        datas['json']['searchName']=searchName
        datas['json']['deal_status']=deal_status

        response = request_init.run_request(**datas)
        assert assert_init.assert_code(response['code'], 200)
        assert assert_init.assert_body(response['body'], 'msg', 'OK')
        assert assert_init.assert_time(response['time_consuming'], 1100)
        consts.RESULT_LIST.append('True')