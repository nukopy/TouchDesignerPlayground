# me - this DAT.
#
# dat - the DAT that received the error
# rowIndex - the row number the error was placed into
# message - the error message
# absFrame - the absolute frame at which the error occured
# frame - the local frame at which the error occured
# severity - describes the level of error (0=info, 1=warning, 2=error, 3=fatal)
# type - describes the family of error
# source - the operator that generated the error


def onError(dat, rowIndex, message, absFrame, frame, severity, type, source):
    print(message)
