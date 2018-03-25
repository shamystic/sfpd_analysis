import numpy as np
zips = [94102, 94103, 94104, 94105, 94107, 94108, 94109, 94110, 94111, 94112, 94114, 94115, 94116, 94117, 94118, 94121, 94122, 94123, 94124, 94127, 94129, 94130, 94131, 94132, 94133, 94134, 94158]
y = 0
for x in zips: 
	print ('<option value="{}">'.format(y) + str(x) + '</option>')
	y += 1

y = 0
b = ['8 AM to 3 PM', '4 PM to 11 PM', '12 AM to 7 AM']
for x in b: 
	print ('<option value="{}">'.format(y) + str(x) + '</option>')
	y += 1

y = 0
b = np.arange(0, 24, 1)
for x in b: 
	print ('<option value="{}">'.format(y) + str(x) + '</option>')
	y += 1

sa = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 28, 29, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 48, 51]
y = 0
for x in sa: 
	print ('<option value="{}">'.format(y) + str(x) + '</option>')
	y += 1