#!/usr/bin/python

import time
import datetime
start_time = time.time()

sum = 0 
for i in range(1000000):
	sum = sum + i

timeElapsed =  time.time() - start_time
print 1.0 / timeElapsed
