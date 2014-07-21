﻿from __future__ import print_function

# Example program to show how to read from a single AtoD channel with default settings
# Marco Forte, 18/06/2014

from atod import AtoD

myAtoD = AtoD()
myAtoD.addChannels([0])
val = myAtoD.readVoltage()
print(val)
