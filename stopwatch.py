import time

#Display the programs instructions.
print('press ENTER to begin. Afterwards, press ENTER to "click" the stopwatch.')
print('Press Ctrl-C to quit.')

print('Started.')
startTime = time.time()
lastTime = startTime
lapNum = 1
try:
	while True:
		input()
		lapTime = round(time.time() - lastTime, 2)
		totalTime = round(time.time() - startTime, 2)
		print('Lap #{}: {} ({})'.format(lapNum, totalTime, lapTime))
		lapNum += 1
		lastTime = time.time() # reset the last lap time
except KeyboardInterrupt:
	# keep Ctrl-C exception from producing error message
	print('\nDone.')




