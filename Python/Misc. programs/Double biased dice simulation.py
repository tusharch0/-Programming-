import random
import pylab as py


def roll():
    return random.choice([1, 2, 3, 4, 4, 4, 5, 6, 6, 6])


ls = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
chance = [104, 203, 302, 401, 505, 646, 756, 855, 985]
for n in chance:
    for k in range(n):
        scr = roll() + roll()
        ls[scr-1] = ls[scr-1] + 4/4


py.figure()
py.plot([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12], ls)

for el in ls:
    print(el)
