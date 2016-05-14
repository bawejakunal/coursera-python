import re,sys

filename = "../Scanner/Interface/ScannerLogs.log"

try:
	handle = open(filename,'r')
	total = 0
	for line in handle:
		if 'FOUND' in line:
			sys.stdout.write(line)
			total +=1 

	print total
except Exception, e:
	raise e