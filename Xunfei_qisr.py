# -*- coding: utf-8 -*-
from ctypes import *

from Xunfei.Xunfei_types import *

api = windll.LoadLibrary("bin/msc_x64.dll")

# 开始一次语音识别
#
# ssb_param = b"ivw_threshold=0:-20,sst=wakeup"
# res = 0
# sesson, res = pyQISRSessionBegin(ssb_param, res)
# print(sesson, res)
#
# const char *MSPAPI 	QISRSessionBegin (const char *grammarList, const char *params, int *errorCode)
def pyQISRSessionBegin(params, errorCode, grammarList=None):
    sessionBg = api.QISRSessionBegin
    sessionBg.restype = c_char_p

    errorCode = c_int(int(errorCode))

    sessionID = sessionBg(c_char_p(grammarList),
                          c_char_p(params),
                          byref(errorCode))

    return errorCode.value, sessionID

# 写入本次识别的音频
#
# waveData = create_string_buffer(b"\0", 5120)
# waveLen = 0
# audioStatus = 2
# EpStatus = 0
# RecogStatus = 0
# EpStatus, RecogStatus, res = pyQISRAudioWrite(sesson, waveData, waveLen, audioStatus, EpStatus, RecogStatus)
# print(EpStatus, RecogStatus, res)
#
# int MSPAPI 	QISRAudioWrite (const char *sessionID, const void *waveData, unsigned int waveLen, int audioStatus, int *epStatus, int *recogStatus)
def pyQISRAudioWrite(sessionID, waveData, waveLen, audioStatus, EpStatus, RecogStatus):
    epStatus = c_int(int(EpStatus))

    recogStatus = c_int(int(RecogStatus))

    res = api.QISRAudioWrite(c_char_p(sessionID),
                              waveData,
                              c_uint(waveLen),
                              c_int(audioStatus),
                              byref(epStatus),
                              byref(recogStatus))

    return epStatus.value, recogStatus.value, res

# 获取识别结果
#
# rsltStatus = 0
# waitTime = 5000
# errorCode = 0
# rsltStatus, errorCode, res = pyQISRGetResult(sesson, rsltStatus, waitTime, errorCode)
# print(rsltStatus, errorCode, res)
#
# const char *MSPAPI 	QISRGetResult (const char *sessionID, int *rsltStatus, int waitTime, int *errorCode)
def pyQISRGetResult(sessionID, RsltStatus, waitTime, ErrorCode):
    getResult = api.QISRGetResult
    getResult.restype = c_char_p

    rsltStatus = c_int(int(RsltStatus))

    errorCode = c_int(int(ErrorCode))

    res = getResult(c_char_p(sessionID),
                    byref(rsltStatus),
                    c_int(waitTime),
                    byref(errorCode))

    return rsltStatus.value, errorCode.value, res

# 结束本次语音识别
#
# hints = b"normal end"
# res = pyQISRSessionEnd(sesson, hints)
# print(res)
#
# int MSPAPI 	QISRSessionEnd (const char *sessionID, const char *hints)
def pyQISRSessionEnd(sessionID, hints):
    return api.QISRSessionEnd(c_char_p(sessionID),
                              c_char_p(hints))

# 获取当次语音识别信息，如上行流量、下行流量等
#
# paramName = b"upflow"
# p_paramValue = pointer(create_string_buffer(b"\0", 32))
# valueLen = 32
# paramValue, valueLen, res= pyQISRGetParam(sesson, paramName, p_paramValue, valueLen)
# print(paramValue, valueLen, res)
#
# int MSPAPI 	QISRGetParam (const char *sessionID, const char *paramName, char *paramValue, unsigned int *valueLen)
def pyQISRGetParam(sessionID, paramName, ParamValue, ValueLen):
    paramValue = ParamValue.contents

    valueLen = c_int(int(ValueLen))

    res = api.QISRGetParam(c_char_p(sessionID),
                           c_char_p(paramName),
                           byref(paramValue),
                           byref(valueLen))

    return paramValue.value, valueLen.value, res

# 构建语法，生成语法ID
#
# int MSPAPI 	QISRBuildGrammar (const char *grammarType, const char *grammarContent, unsigned int grammarLength, const char *params, GrammarCallBack callback, void *userData)
def _pyQISRBuildGrammar(grammarType, grammarContent, grammarLength, params, callback, UserData):
    pass

# 更新本地语法词典
#
# int MSPAPI 	QISRUpdateLexicon (const char *lexiconName, const char *lexiconContent, unsigned int lexiconLength, const char *params, LexiconCallBack callback, void *userData)
def _pyQISRUpdateLexicon(lexiconName, lexiconContent, lexiconLength, params, callback, userData):
    pass

