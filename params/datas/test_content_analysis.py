#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2020/3/18 14:08
# @Author  : Mcen (mmocheng@163.com)
# @Name    : test_content_analysis

class D:
    @classmethod
    def dayCount(self):
        # 告警类型统计图中天数
        return [1,7,30,9999]

    @classmethod
    def buildingId(self):
        # buildingId为空时，是校企，不为空时是建筑
        return ['','7892677051232747520']

    @classmethod
    def end_start(self):
        return [('-1','2020-01-01','2020-03-18')]

    @classmethod
    def month(self):
        return [1,2,3,4,5,6,7,8,9,10.11,12]

    @classmethod
    def year(self):
        return [2019,2020]

    @classmethod
    def buildingId_flag(self):
        # flag为true就是校企下的搜索，flag为false就是建筑下的搜索
        return [('','true'),('7892677051232747520','false')]