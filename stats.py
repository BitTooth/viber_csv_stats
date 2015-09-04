from csv_parser import buildMessagesArray
import operator

messages = buildMessagesArray("Nastya.csv", True)
out = open("stats.txt", "w")

# read ignored words
ignoredFile = open("ignore_words.list", "r")
ignoredWords = []
for line in ignoredFile:
	ignoredWords.append(line[:-1])

delimeters = ".,\\/><[]{}()!@#$%^&*:;\"\'?1234567890\n"
def GenerateWordsCloud(messages):
	# clear messages from delimeters
	for d in delimeters:
		for message in messages:
			message._message = message._message.replace(d, ' ').lower()

	# generate most used words dictionary
	word_map = {}
	for message in messages:
		for word in message._message.split( ):
			if word in word_map.keys():
				word_map[word] = word_map[word] + 1
			else:
				word_map[word] = 1

	# and sort it
	sorted_map = reversed(sorted(word_map.items(), key=operator.itemgetter(1)))

	return sorted_map

def PrintCloud(output, words):
	for word in words:
		if len(word[0]) > 2 and word[1] > 2 and word[0].lower() not in ignoredWords:
			output.write(word[0] + '(' + str(word[1]) + ') ')
	output.write('\n\n\n\n')

############################################################################################################
# 1. First messages and number and length of messages

# Gather stats
first = messages[0]
last = messages[0]

messagesNum = len(messages)
myMessages = []
partnerMessages = []
myMessagesLength = 0
partnerMessagesLength = 0

for msg in messages:
	# find first and last message time
	if msg._datetime < first._datetime:
		first = msg

	if msg._datetime > last._datetime:
		last = msg

	# find number and length of messages
	if len(msg._author) == 1: # f*cking unicode
		myMessages.append(msg)
		myMessagesLength = myMessagesLength + len(msg._message)
	else:
		partnerMessages.append(msg)
		partnerMessagesLength = partnerMessagesLength + len(msg._message)

myMessagesNum = len(myMessages)
partnerMessagesNum = len(partnerMessages)

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
# 2. Timeline stats

timeline = {}

for i in range(0, 24):
	timeline[i] = 0

for msg in messages:
	timeline[msg._datetime.hour] = timeline[msg._datetime.hour] + 1

out.write("\nTimeline of messages\n")
for i in range(0, 24):
	out.write(str(i) + ': ' + str(timeline[i]) + '\n')

###############################################################################################################
# 3. Word cloud

out.write("\nAll words cloud:\n")
allWords = GenerateWordsCloud(messages)
PrintCloud(out, allWords)

out.write("\nMy words cloud:\n")
myWords = GenerateWordsCloud(myMessages)
PrintCloud(out, myWords)

out.write("\nPartner words cloud:\n")
partnerWords = GenerateWordsCloud(partnerMessages)
PrintCloud(out, partnerWords)