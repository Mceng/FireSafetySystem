#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2020/3/17 17:21
# @Author  : Mcen (mmocheng@163.com)
# @Name    : test_MonitoringSupervise

class D:
    @classmethod
    def warningManger_pass(self):
        # 告警处理\审核\综合查询界面获取的正常数据
        return [
        ([0, 1, 2],"true"),#处理
        ([3],"true"),#审核
        ([0, 1, 2, 3],"true")#综合查询
    ]

    @classmethod
    def connectStatus_runStatus_deviceStatus_enabled(self):
        return [["0", "1"],["0"],["1"],[]]

    @classmethod
    def target(self):
        """
        0监控中心
        1监测点管理
        2告警管理
        :return:
        """

        return ["1","0"]
    @classmethod
    def searchName(self):
        return ["4","消火栓","消火栓",""]

    @classmethod
    def type(self):
        return [["1"],["2"],["3"],["4"],["5"],["6"],[]]

    @classmethod
    def deal_status(self):
        return [[0, 1, 2],[3],[0, 1, 2, 3]]


    def Matching_s_pass(self):
        # 通过搜索获取设备的卡片信息数据
        # buildingId: "7892677051232747520"
        # connectStatus: []
        # customerId: "7892661029798871040"
        # deviceStatus: ["1"]
        # enabled: []
        # runStatus: []
        # searchName: ""
        # target: "0"
        # type: ["2"]

        buildingId: "7892677051232747520"
        connectStatus: []
        customerId: "7892661029798871040"

        flag: true
        deviceStatus: ["0"]
        enabled: []
        runStatus: []
        searchName: ""
        target: "2"
        type: []


        # buildingId: "7892677051232747520"
        # connectStatus: ["0", "1"]
        # customerId: "7892661029798871040"
        # deal_status: [3]
        # deviceStatus: ["0", "1"]
        # enabled: ["0", "1"]
        # flag: true
        # runStatus: ["0", "1"]
        # searchName: ""
        # target: "2"
        # type: ["2"]

        data = [
            (["0", "1"],[3],["0", "1"],["0", "1"],["0", "1"],"2",["2"])
        ]
        return data