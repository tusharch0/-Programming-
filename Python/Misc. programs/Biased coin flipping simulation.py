import random
import pylab as py


def flip():
    return random.choice(['H', 'H', 'H', 'T', 'T', 'H', 'T'])


ls = [0, 0]
chance = [104, 203, 302, 401, 505, 646, 756, 855, 985, 4565, 6565]
for n in chance:
    for k in range(n):
        scr = flip()
        if scr == 'H':
            ls[0] = ls[0] + 4/4
        else:
            ls[1] = ls[1] + 4/4


py.figure()
py.plot(['H', 'T'], ls, 'bo')
py.ylim(0, 12300)

print("HEADS: ", ls[0])
print("TAILS: ", ls[1])
