import csv
import datetime
from messages import *

def buildMessagesArray(filename, debugOutput = False):
	print 'Building array from csv'
	messages = [] 		
	prevMessage = None 	# previous message used for concat multiline messages

	with open(filename, "rb") as csvfile:
		rdr = csv.reader(csvfile, skipinitialspace=True, quoting=csv.QUOTE_ALL)

		for row in rdr:
			values = list(row)

			if len(values) == 0:
				continue

			# Check whether the new row is just continue of multiline message
			# Use first date field as indicator of new message. Yeah, it's a little bit hacky
			if not isDateField(values[0]) and prevMessage is not None:
				for value in values:
					prevMessage._message.join(' ' + value.decode('string-escape').decode("utf-8") + '\n')
			else:
				date = row[0]
				time = row[1]
				author = row[2]
				message = ''

				for value in values[4:]:
					message = message + ', ' + value
				message = message + '\n'

				msg = Message(author, date, time, message[2:].decode('string-escape').decode("utf-8"))
				prevMessage = msg
				messages.append(msg)

	if debugOutput:
		out = open ("debug.txt", "w")
		for msg in messages:
			msg.out(out, True)

	return messages