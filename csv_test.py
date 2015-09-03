import csv
import datetime

class Message:
	def __init__(self, author, date, time, message):
		self._author = author
		self._date = date
		self._time = time
		self._message = message

def isDateField(field):
	try:
		datetime.datetime.strptime(field, '%d/%m/%Y')
		return True
	except ValueError:
		return False

out = open ("out.txt", "w")

messages = [] 		
prevMessage = None 	# previous message used for concat multiline messages

with open("Nastya.csv", "rb") as csvfile:
	rdr = csv.reader(csvfile, skipinitialspace=True, quoting=csv.QUOTE_ALL)

	for row in rdr:
		values = list(row)

		if len(values) == 0:
			continue

		# Check whether the new row is just continue of multiline message
		# Use first date field as indicator of new message. Yeah, it's a little bit hacky
		if not isDateField(values[0]) and prevMessage is not None:
			for value in values:
				prevMessage._message.join(' ' + value + '\n')
		else:
			date = row[0]
			time = row[1]
			author = row[2]
			message = ''

			for value in values[4:]:
				message = message + ', ' + value
			message = message + '\n'

			msg = Message(author, date, time, message[2:])
			prevMessage = msg
			messages.append(msg)

for msg in messages:
	out.write(msg._date + ' ' + msg._time + '\n' + msg._author + '\n' + msg._message)
	out.write("\n=========================================================================\n")