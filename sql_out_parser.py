# coding: utf8
from messages import *
import codecs

f = open('names.conf')
myName = f.readline()[:-1]
partnerName = f.readline()[:-1]

def buildMessagesArray(filename, debugOutput = False):
	print 'Building array from db'
	f = open(filename, 'r')

	lines = []
	line = f.readline()
	while line <> '':
		lines.append(line)
		line = f.readline()

	messages = []
	prevMessage = None 	# used to concat multiline messages

	for line in lines:
		tokens = line.split('|')
		if isDateTimestampField(tokens[0]):
			# new message
			msg = Message()
			msg._author = myName if tokens[1] == '1' else partnerName
			msg._datetime = datetime.datetime.fromtimestamp(int(tokens[0]))
			msg._message = tokens[3].decode('string-escape').decode("utf-8") #.decode('utf-8')

			messages.append(msg)
			prevMessage = msg

		else:
			# new line of previous message
			prevMessage._message += u'\n' + line.decode('utf-8')

	if debugOutput:
		out = open('debug_db.txt', 'w')
		for msg in messages:
			msg.out(out, True)

	return messages
			

if __name__ == '__main__':
	array = buildMessagesArray('messages.log', True)
