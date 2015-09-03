import csv

out = open ("out.txt", "w")
filename = "Nastya.csv"

with open(filename, "rb") as csvfile:
	rdr = csv.reader(csvfile, skipinitialspace=True, quoting=csv.QUOTE_ALL)

	for row in rdr:
		out.write('\n=================================================================================================\n')
		values = list(row)
		for value in values:
			out.write(value + '\n')