# -*- coding: utf-8 -*-
from ctypes import *

from Xunfei.Xunfei_types import *

api = windll.LoadLibrary("bin/msc_x64.dll")

# 初始化msc，用户登录
#
# lgi_param = b"appid = xxx,engine_start = ivw,ivw_res_path =fo|res/ivw/wakeupresource.jet, work_dir = ."
# res  = pyMSPLogin(lgi_param)
#
# int MSPAPI 	MSPLogin (const char *usr, const char *pwd, const char *params)
def pyMSPLogin(params, usr=None, pwd=None):
    return api.MSPLogin(c_char_p(usr),
                        c_char_p(pwd),
                        c_char_p(params))

# 退出登录
#
# int MSPAPI 	MSPLogout ()
def pyMSPLogout():
    return api.MSPLogout()

# 参数设置接口、离线引擎初始化接口
#
# int MSPAPI 	MSPSetParam (const char *paramName, const char *paramValue)
def pyMSPSetParam(paramName, paramValue):
    return api.MSPSetParam(c_char_p(paramName),
                           c_char_p(paramValue))

# 获取MSC的设置信息
#
# para_name = b"upflow"
# para_value = create_string_buffer(b"\0", 32)
# value_len = 32
# Len, res = pyMSPGetParam(para_name, para_value, value_len)
#
# int MSPAPI 	MSPGetParam (const char *paramName, char *paramValue, unsigned int *valueLen)
def pyMSPGetParam(paramName, paramValue, Len):
    valueLen = c_int(int(Len))

    res = api.MSPGetParam(c_char_p(paramName),
                          paramValue,
                          byref(valueLen))

    return valueLen.value, res
