# -*- coding: utf-8 -*-
from ctypes import *

from Xunfei.Xunfei_types import *

api = windll.LoadLibrary("bin/msc_x64.dll")

# 开始唤醒功能，并在参数中指定唤醒(唤醒+识别时)用到的语法列表，本次唤醒所用的参数等
#
# errorCode = 0
# errorCode, sessionID = pyQIVWSessionBegin(ssb_param, errorCode)
# print(errorCode, sessionID)
#
# const char *MSPAPI 	QIVWSessionBegin (const char *grammarList, const char *params, int *errorCode)
def pyQIVWSessionBegin(params, ErrorCode, grammarList=None):
    sessionBg = api.QIVWSessionBegin
    sessionBg.restype = c_char_p

    errorCode = c_int(int(ErrorCode))

    sessionID = sessionBg(c_char_p(grammarList),
                          c_char_p(params),
                          byref(errorCode))

    return errorCode.value, sessionID

# 结束本次语音唤醒
#
# hints = b"normal end"
# res = pyQIVWSessionEnd(sessionID, hints)
# print(res)
#
# int MSPAPI 	QIVWSessionEnd (const char *sessionID, const char *hints)
def pyQIVWSessionEnd(sessionID, hints):
    return api.QIVWSessionEnd(c_char_p(sessionID),
                              c_char_p(hints))

# 写入本次唤醒的音频，本接口需要反复调用直到音频写完为止
#
# int MSPAPI 	QIVWAudioWrite (const char *sessionID, const void *audioData, unsigned int audioLen, int audioStatus)
def pyQIVWAudioWrite(sessionID, audioData, audioLen, audioStatus):
    return api.QIVWAudioWrite(c_char_p(sessionID),
                              c_char_p(audioData),
                              c_uint(audioLen),
                              c_int(audioStatus))

def py_ivw_ntf_handler(sessionID, msg, param1, param2, info, userData):
    if MSP_IVW_MSG_ERROR == msg:
        print("error")
    elif MSP_IVW_MSG_WAKEUP == msg:
        print("success")
    return 0

CMPFUNC = CFUNCTYPE(c_int, POINTER(c_char), c_int, c_int, c_int, c_void_p, c_void_p)

# 注册回调
#
# int MSPAPI 	QIVWRegisterNotify (const char *sessionID, ivw_ntf_handler msgProcCb, void *userData)
def pyQIVWRegisterNotify(sessionID, userData=None):
    return api.QIVWRegisterNotify(c_char_p(sessionID),
                                  CMPFUNC(py_ivw_ntf_handler),
                                  c_void_p(userData))
