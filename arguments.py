# Class for the single argument to store argument's params
class Arg:
	_name = ""				# name of the argument
	_key = ""				# key of the argument to be switched via command line
	_isBool = False			# wether this key can be only on/off or next argument in list will be used as value
	_value = None			# current value of the argument parsed from list
	_defaultValue = None	# default value before parsing or after reseting
	_help = ""				# help message for the help screen

	def __init__(self, name, key, help = "", isBool = False, defaultValue = None):
		self._name = name
		self._key = key
		self._isBool = isBool
		self._help = help

		if isBool:	self._defaultValue = False
		else:		self._defaultValue = defaultValue

		self._value = self._defaultValue

class Arguments:
	args = []					# list of arguments. Instances of Args class
	errorCallback = None		# callback to be used if custom error output needed

	def __init__(self, errorCallback=None):
		self.errorCallback = errorCallback if errorCallback is not None else self.__defaultErrorOutput

	def __defaultErrorOutput(self, message):
		print message

	def setErrorCallback(errorCallback):
		self.errorCallback = errorCallback

	def addArg(self, arg):
		self.args.append(arg)

	def addNewArg(self, name, key, help = "", isBool = False, defaultValue = None):
		arg = Arg(name, key, help, isBool, defaultValue)
		self.addArg(arg)

	def getValue(self, name):
		arg = self.findArgByName(name)
		return arg._value if arg is not None else None

	def findArgByKey(self, key):
		try:
			return next(arg for arg in self.args if arg._key == key)
		except StopIteration:
			return None

	def findArgByName(self, name):
		try:
			return next(arg for arg in self.args if arg._name == name)
		except StopIteration:
			return None

	def resetValues(self):
		for a in self.args:
			a._value = a._defaultValue

	def parseArgs(self, arguments, stopOnError = False):
		nextIsValue = False
		currentArg = None
		for arg in arguments:
			if nextIsValue:
				if currentArg is not None:
					currentArg._value = arg
					nextIsValue = False
					currentArg = None
					continue
				else:
					self.errorCallback("Error parsing argument value {0}. No current arg".format(arg))
					if stopOnError:
						return False

			a = self.findArgByKey(arg)
			if a is not None:
				if a._isBool:
					a._value = True
				else:
					nextIsValue = True
					currentArg = a
			else:
				self.errorCallback("Error parsing argument {0}. Did you forget to add it define?".format(arg))
				if stopOnError:
					return False

		return True

	def printHelp(self, printCallback = None):
		for a in self.args:
			if printCallback is None:
				print '{0} ({1})\t- {2}'.format(a._key, a._name, a._help)
			else:
				printCallback(a._name, a._key, a._help)




