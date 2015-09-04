from csv_parser import buildMessagesArray
messages = buildMessagesArray("Nastya.csv", True)
out = open("stats.txt", "w")

############################################################################################################
# 1. First messages and number and length of messages

# Gather stats
first = messages[0]
last = messages[0]

messagesNum = len(messages)
myMessagesNum = 0
myMessagesLength = 0
partnerMessagesNum = 0
partnerMessagesLength = 0

for msg in messages:
	# find first and last message time
	if msg._datetime < first._datetime:
		first = msg

	if msg._datetime > last._datetime:
		last = msg

	# find number and length of messages
	if len(msg._author) == 1: # f*cking unicode
		myMessagesNum = myMessagesNum + 1
		myMessagesLength = myMessagesLength + len(msg._message)
	else:
		partnerMessagesNum = partnerMessagesNum + 1
		partnerMessagesLength = partnerMessagesLength + len(msg._message)

days = (last._datetime - first._datetime).days
myAverageMsgLength = myMessagesLength / myMessagesNum
partnerAverageMsgLength = partnerMessagesLength / partnerMessagesNum

# output stats
out.write("First message was " + str(first._datetime) + '\n')
out.write("Last message was " + str(last._datetime) + '\n')
out.write("Whole number of days: " + str(days) + '\n')

out.write("\nNumber of messages: " + str(messagesNum) + '\n')

out.write("Average number of messages per day: " + str(messagesNum / days) + '\n')

myMsgPercentage = myMessagesNum * 100 / messagesNum
out.write("\nMy messages number: " + str(myMessagesNum) + ' [' + str(myMsgPercentage) + '%]\n')
out.write("Partner messages number: " + str(partnerMessagesNum) + ' [' + str(100 - myMsgPercentage) + '%]\n')

out.write("\nMy average message length: " + str(myAverageMsgLength) + '\n')
out.write("Partner average message length: " + str(partnerAverageMsgLength) + '\n')

###############################################################################################################
