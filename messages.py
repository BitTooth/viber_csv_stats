import datetime

class Message:

	def __init__(self, author='', date='', time='', message=''):
		self._author = author
		try:
			self._datetime = datetime.datetime.strptime(date + ' ' + time, "%d/%m/%Y %H:%M:%S")
		except ValueError:
			self._datetime = None
		self._message = message

	def __eq__(self, other):
		return self._message == other._message

	def __ne__(self, other):
		return self._message != other._message

	def __hash__(self):
		return hash(self._message)
		return int((self._datetime - datetime.datetime(1970,1,1)).total_seconds())

	def __cmp__(self, other):
		return int((self._datetime - datetime.datetime(1970,1,1)).total_seconds()) - \
		int((other._datetime - datetime.datetime(1970,1,1)).total_seconds())

	def out(self, outFile = None, useDecoding = False):
		if useDecoding:
			text = self._message.encode('utf-8')
		else:
			text = self._message

		line = str(self._datetime) + '\n' + self._author + '\n' + text + \
		"\n=========================================================================\n"

		if outFile is not None:
			outFile.write(line)
		else:
			print line

def isDateField(field):
	try:
		datetime.datetime.strptime(field, '%d/%m/%Y')
		return True
	except ValueError:
		return False

def isDateTimestampField(field):
	try:
		timestamp = int(field)
		datetime.datetime.fromtimestamp(timestamp)
		return True;
	except ValueError:
		return False

def makeUnitedArray(arr1, arr2):
	print 'Uniting arrays'
	# arr1.extend(arr2)
	res = list(set(arr1) | set(arr2))
	res.sort()
	return res
