# -*- coding: utf-8 -*-
from ctypes import *

from Xunfei.Xunfei_types import *

api = windll.LoadLibrary("bin/msc_x64.dll")

# 开始一次语音合成，分配语音合成资源
#
# const char *MSPAPI 	QTTSSessionBegin (const char *params, int *errorCode)
def pyQTTSSessionBegin(params):
    errorCode = c_int()

    res = api.QTTSSessionBegin(c_char_p(params),
                               byref(errorCode))

    return errorCode.value, res

# 写入要合成的文本
#
# QTTSTextPut (const char *sessionID, const char *textString, unsigned int textLen, const char *params)
def pyQTTSTextPut(sessionID, TextString, params=None):
    textString = TextString.encode("utf-8")

    textLen = len(TextString)

    return api.QTTSTextPut(c_char_p(sessionID),
                           c_char_p(textString),
                           c_uint(textLen),
                           c_char_p(params))

# 获取合成音频
#
# const void *MSPAPI 	QTTSAudioGet (const char *sessionID, unsigned int *audioLen, int *synthStatus, int *errorCode)
def pyQTTSAudioGet(sessionID, AudioLen, SynthStatus, ErrorCode):
    audioGet = api.QTTSAudioGet
    audioGet.restype = c_void_p

    audioLen = c_uint(int(AudioLen))

    synthStatus = c_int(int(SynthStatus))

    errorCode = c_int(int(ErrorCode))

    res = audioGet(c_char_p(sessionID),
                   byref(audioLen),
                   byref(synthStatus),
                   byref(errorCode))

    return audioLen.value, synthStatus.value, errorCode.value, res

# 结束本次语音合成
#
# int MSPAPI 	QTTSSessionEnd (const char *sessionID, const char *hints)
def pyQTTSSessionEnd(sessionID, hints):
    return api.QTTSSessionEnd(c_char_p(sessionID),
                              c_char_p(hints))

# 获取当前语音合成信息，如当前合成音频对应文本结束位置、上行流量、下行流量等
#
# int MSPAPI 	QTTSGetParam (const char *sessionID, const char *paramName, char *paramValue, unsigned int *valueLen)
def pyQTTSGetParam(sessionID, paramName, ParamValue, ValueLen):
    paramValue = c_char_p(ParamValue)

    valueLen = c_uint(int(ValueLen))

    res = api.QTTSGetParam(c_char_p(sessionID),
                           c_char_p(paramName),
                           byref(paramValue),
                           byref(valueLen))

    return paramValue.value, valueLen.value, res
