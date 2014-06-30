﻿# Marco Forte, 18/06/2014
# Tests digital IO and counter - and sends a sequence of o's and 1's on P0.0 and counts them
# Connect P0.0 to PFIO counter with a wire!

from Digital_IO import *
from Counter import *
from time import sleep


myCounter = Counter()
myDigital_IO = Digital_IO()

myCounter.start()

for i in range(666):
    myDigital_IO.write(0)
    sleep(0.0001)
    myDigital_IO.write(1)
print(myCounter.stop())