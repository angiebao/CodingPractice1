# def topNCompetitors(numCompetitors, topNCompetitors, competitors,
#                     numReviews, reviews):
#     # WRITE YOUR CODE HERE
#

# def reorderLines(logFileSize, logLines):
#     # WRITE YOUR CODE HERE
#     log_string = []
#     log_number = []
#
#     for i in range(logFileSize):
#         log = logLines[i].split(' ', 1)
#         if log[1][0].isdigit():
#             log_number.append(log)
#
#         else:
#             log_string.append(log)
#
#     log_string.sort(key=lambda x: (x[1].lower(), x[0].lower()))
#
#     result = log_string + log_number
#     # regenerate the result
#     result = [item[0] + ' ' + item[1] for item in result]
#     return result

def reorderLines(logFileSize, logLines):
    log_string = []
    log_number = []
    for i in range(logFileSize):
        log =  logLines[i].split(' ',1) # split identifier with the following numbers or words
        if log[1][0].isnumeric():
            log_number.append(log)

        else:
            log_string.append(log)

    # sort the log_string, if there is tie, sort by identifier
    log_string.sort(key = lambda x: (x[1].lower(), x[0].lower()))
    result = log_string + log_number # list 可以直接相加

    return [item[0] + ' ' + item[1] for item in result]

    # now

logFileSize = 3
logLines=["g1 afdg SDGA sgewetg",
         "a2 1043 24395 ",
         "d2 ghwo geoj"]


print(reorderLines(logFileSize, logLines))