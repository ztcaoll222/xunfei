# -*- coding: utf-8 -*-
'''
/**
 *  MSPSampleStatus indicates how the sample buffer should be handled
 *  MSP_AUDIO_SAMPLE_FIRST		- The sample buffer is the start of audio
 *								  If recognizer was already recognizing, it will discard
 *								  audio received to date and re-start the recognition
 *  MSP_AUDIO_SAMPLE_CONTINUE	- The sample buffer is continuing audio
 *  MSP_AUDIO_SAMPLE_LAST		- The sample buffer is the end of audio
 *								  The recognizer will cease processing audio and
 *								  return results
 *  Note that sample statii can be combined; for example, for file-based input
 *  the entire file can be written with SAMPLE_FIRST | SAMPLE_LAST as the
 *  status.
 *  Other flags may be added in future to indicate other special audio
 *  conditions such as the presence of AGC
 */
'''
MSP_AUDIO_SAMPLE_INIT = 0x00
MSP_AUDIO_SAMPLE_FIRST = 0x01
MSP_AUDIO_SAMPLE_CONTINUE = 0x02
MSP_AUDIO_SAMPLE_LAST = 0x04

'''
/**
 *  The enumeration MSPRecognizerStatus contains the recognition status
 *  MSP_REC_STATUS_SUCCESS				- successful recognition with partial results
 *  MSP_REC_STATUS_NO_MATCH				- recognition rejected
 *  MSP_REC_STATUS_INCOMPLETE			- recognizer needs more time to compute results
 *  MSP_REC_STATUS_NON_SPEECH_DETECTED	- discard status, no more in use
 *  MSP_REC_STATUS_SPEECH_DETECTED		- recognizer has detected audio, this is delayed status
 *  MSP_REC_STATUS_COMPLETE				- recognizer has return all result
 *  MSP_REC_STATUS_MAX_CPU_TIME			- CPU time limit exceeded
 *  MSP_REC_STATUS_MAX_SPEECH			- maximum speech length exceeded, partial results may be returned
 *  MSP_REC_STATUS_STOPPED				- recognition was stopped
 *  MSP_REC_STATUS_REJECTED				- recognizer rejected due to low confidence
 *  MSP_REC_STATUS_NO_SPEECH_FOUND		- recognizer still found no audio, this is delayed status
 */
'''
MSP_REC_STATUS_SUCCESS = 0
MSP_REC_STATUS_NO_MATCH = 1
MSP_REC_STATUS_INCOMPLETE = 2
MSP_REC_STATUS_NON_SPEECH_DETECTED = 3
MSP_REC_STATUS_SPEECH_DETECTED = 4
MSP_REC_STATUS_COMPLETE = 5
MSP_REC_STATUS_MAX_CPU_TIME = 6
MSP_REC_STATUS_MAX_SPEECH = 7
MSP_REC_STATUS_STOPPED = 8
MSP_REC_STATUS_REJECTED = 9
MSP_REC_STATUS_NO_SPEECH_FOUND = 10
MSP_REC_STATUS_FAILURE = MSP_REC_STATUS_NO_MATCH


'''
/**
 * The enumeration MSPepState contains the current endpointer state
 *  MSP_EP_LOOKING_FOR_SPEECH	- Have not yet found the beginning of speech
 *  MSP_EP_IN_SPEECH			- Have found the beginning, but not the end of speech
 *  MSP_EP_AFTER_SPEECH			- Have found the beginning and end of speech
 *  MSP_EP_TIMEOUT				- Have not found any audio till timeout
 *  MSP_EP_ERROR				- The endpointer has encountered a serious error
 *  MSP_EP_MAX_SPEECH			- Have arrive the max size of speech
 */
'''
MSP_EP_LOOKING_FOR_SPEECH = 0
MSP_EP_IN_SPEECH = 1
MSP_EP_AFTER_SPEECH = 3
MSP_EP_TIMEOUT = 4
MSP_EP_ERROR = 5
MSP_EP_MAX_SPEECH = 6
MSP_EP_IDLE = 7


'''
/* Synthesizing process flags */
'''
MSP_TTS_FLAG_STILL_HAVE_DATA = 1
MSP_TTS_FLAG_DATA_END = 2
MSP_TTS_FLAG_CMD_CANCELED = 4


'''
/* Handwriting process flags */
'''
MSP_HCR_DATA_FIRST = 1
MSP_HCR_DATA_CONTINUE = 2
MSP_HCR_DATA_END = 4


'''
/*ivw message type */
'''
MSP_IVW_MSG_WAKEUP = 1
MSP_IVW_MSG_ERROR = 2
MSP_IVW_MSG_ISR_RESULT = 3
MSP_IVW_MSG_ISR_EPS = 4
MSP_IVW_MSG_VOLUME = 5
MSP_IVW_MSG_ENROLL = 6
MSP_IVW_MSG_RESET = 7


'''
/* Upload data process flags */
'''
MSP_DATA_SAMPLE_INIT = 0x00
MSP_DATA_SAMPLE_FIRST = 0x01
MSP_DATA_SAMPLE_CONTINUE = 0x02
MSP_DATA_SAMPLE_LAST = 0x04

MSP_SUCCESS = 0
MSP_ERROR_FAIL = -1
MSP_ERROR_EXCEPTION = -2

'''
/* General errors 10100(0x2774) */
'''
MSP_ERROR_GENERAL						= 10100 	# /* 0x2774 */
MSP_ERROR_OUT_OF_MEMORY					= 10101	    # /* 0x2775 */
MSP_ERROR_FILE_NOT_FOUND				= 10102	    # /* 0x2776 */
MSP_ERROR_NOT_SUPPORT					= 10103 	# /* 0x2777 */
MSP_ERROR_NOT_IMPLEMENT					= 10104 	# /* 0x2778 */
MSP_ERROR_ACCESS						= 10105 	# /* 0x2779 */
MSP_ERROR_INVALID_PARA					= 10106 	# /* 0x277A */  /* 缺少参数 */
MSP_ERROR_INVALID_PARA_VALUE			= 10107 	# /* 0x277B */  /* 无效参数值 */
MSP_ERROR_INVALID_HANDLE				= 10108 	# /* 0x277C */
MSP_ERROR_INVALID_DATA					= 10109 	# /* 0x277D */
MSP_ERROR_NO_LICENSE					= 10110 	# /* 0x277E */  /* 引擎授权不足 */
MSP_ERROR_NOT_INIT						= 10111 	# /* 0x277F */  /* 引擎未初始化,可能是引擎崩溃 */
MSP_ERROR_NULL_HANDLE					= 10112 	# /* 0x2780 */
MSP_ERROR_OVERFLOW						= 10113 	# /* 0x2781 */  /* 单用户下模型数超上限(10个), */
                                                                 #  /* 只出现在测试时对一个用户进行并发注册 */
MSP_ERROR_TIME_OUT						= 10114 	# /* 0x2782 */  /* 超时 */
MSP_ERROR_OPEN_FILE						= 10115 	# /* 0x2783 */
MSP_ERROR_NOT_FOUND						= 10116 	# /* 0x2784 */  /* 数据库中模型不存在 */
MSP_ERROR_NO_ENOUGH_BUFFER				= 10117 	# /* 0x2785 */
MSP_ERROR_NO_DATA						= 10118 	# /* 0x2786 */  /* 从客户端读音频或从引擎段获取结果时无数据 */
MSP_ERROR_NO_MORE_DATA					= 10119 	# /* 0x2787 */
MSP_ERROR_NO_RESPONSE_DATA				= 10120 	# /* 0x2788 */
MSP_ERROR_ALREADY_EXIST					= 10121 	# /* 0x2789 */  /* 数据库中模型已存在 */
MSP_ERROR_LOAD_MODULE					= 10122 	# /* 0x278A */
MSP_ERROR_BUSY							= 10123 	# /* 0x278B */
MSP_ERROR_INVALID_CONFIG				= 10124 	# /* 0x278C */
MSP_ERROR_VERSION_CHECK                 = 10125 	# /* 0x278D */
MSP_ERROR_CANCELED						= 10126 	# /* 0x278E */
MSP_ERROR_INVALID_MEDIA_TYPE			= 10127 	# /* 0x278F */
MSP_ERROR_CONFIG_INITIALIZE				= 10128 	# /* 0x2790 */
MSP_ERROR_CREATE_HANDLE					= 10129 	# /* 0x2791 */
MSP_ERROR_CODING_LIB_NOT_LOAD			= 10130 	# /* 0x2792 */
MSP_ERROR_USER_CANCELLED				= 10131 	# /* 0x2793 */
MSP_ERROR_INVALID_OPERATION				= 10132 	# /* 0x2794 */
MSP_ERROR_MESSAGE_NOT_COMPLETE			= 10133	    # /* 0x2795 */   /* flash */
MSP_ERROR_NO_EID						= 10134	    # /* 0x2795 */
MSP_ERROE_OVER_REQ                      = 10135     # /* 0x2797 */   /* client Redundancy request */
MSP_ERROR_USER_ACTIVE_ABORT             = 10136     # /* 0x2798 */   /* user abort */
MSP_ERROR_BUSY_GRMBUILDING              = 10137     # /* 0x2799 */
MSP_ERROR_BUSY_LEXUPDATING              = 10138     # /* 0x279A */
MSP_ERROR_SESSION_RESET	                = 10139     # /* 0x279B */   /* msc主动终止会话，准备重传 */
MSP_ERROR_BOS_TIMEOUT                   = 10140     # /* 0x279C */   /* VAD前端点超时 */
MSP_ERROR_STREAM_FILTER					= 10141  	# /* 0X279D */   /* AIUI当前Stream被过滤 */
MSP_ERROR_STREAM_CLEAR				    = 10142     # /* 0X279E */   /* AIUI当前Stream被清理 */
