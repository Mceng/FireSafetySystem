#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2020/3/18 10:32
# @Author  : Mcen (mmocheng@163.com)
# @Name    : test_content_warningManger

class D:
    @classmethod
    def get_type(self):
        return [1,2,3,4,5]

    @classmethod
    def get_Alarm_dealType(self):
        return [[0, 1, 2],[2],[0, 1, 2, 3],["0", "1", "3", "2"],["0"],["1"],["2"],["3"]]

    @classmethod
    def get_DealFrom_dealType(self):
        return [[2, 3, 4, 8],[3, 6, 7],[2, 3, 4, 5, 6, 7, 8],["8", "2", "3", "4", "5", "6", "7"],["8", "2"],["3", "6", "7"],["4"],["5"]]