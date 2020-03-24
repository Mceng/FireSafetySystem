#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2020/3/10
# @Author  : Mcen (mmocheng@163.com)
# @Name    : conftest

import pytest
from utils.common import CommonUtil
from base.oper_token import OperToken
from utils.Request import Request
from utils.Assert import Assertions
from base.get_params import GetParams
from base import consts
from utils.data_cleanup import Data_Cleanup
from config.config import Config


# blocker级别：中断缺陷（客户端程序无响应，无法执行下一步操作）
# critical级别：临界缺陷（ 功能点缺失）
# normal级别：普通缺陷（数值计算错误）
# minor级别：次要缺陷（界面错误与UI需求不符）
# trivial级别：轻微缺陷（必输项无提示，或者提示不规范）

@pytest.fixture(scope='session')
def common_init():
    return CommonUtil()


@pytest.fixture(scope='session')
def params_init():
    return GetParams()


@pytest.fixture(scope='session')
def request_init():
    return Request()


@pytest.fixture(scope='session')
def assert_init():
    return Assertions()

@pytest.fixture(scope='session', autouse=True)
def session_init():
    """
    数据准备
    :return:
    """
    env = consts.API_ENV_DEBUG
    # 1、生成环境
    env_key=Config().get_env(env)
    CommonUtil().generate_environment(env_key)

    # 2、cookie准备
    OperToken().generate_cookie(env)



    yield
    # 后置操作
    # Data_Cleanup.data_cleanup()
    print(consts.TIMES_LIST)
