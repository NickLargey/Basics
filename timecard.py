import time


startTime = time.time()
nameList = {}

try:
	while True:
		
		name = input('Enter a name: ').upper()
		if name not in nameList:
			startTime
			nameList.update({name: startTime})
			print(nameList)

		
		elif name in nameList:
			print(startTime)
			print(int(time.time())
			print('You worked {} hours today.'.format(round(((time.time() - startTime)/3600.0),3)))
			nameList.pop(name)
			print(nameList)

except KeyboardInterrupt:
	print('\nGood-Bye!')


