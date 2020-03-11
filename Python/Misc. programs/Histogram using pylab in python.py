import random
import pylab
val = []

for n in range(1004):
    x = random.choice(range(0, 90))
    y = random.choice(range(0, 90))
    val.append(x+y)

pylab.hist(val, bins=10)
pylab.xlabel('NUMBER OF OCCURENCE')
