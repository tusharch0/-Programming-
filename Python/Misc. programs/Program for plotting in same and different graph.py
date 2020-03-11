import pylab as pl

#PLOTTING IN SAPERATE GRAPH
pl.figure(1)
pl.plot([1, 2, 3], [1, 2, 3, ])
#PLOTTING IN SAPERATE GRAPH
pl.figure(2)
pl.plot([1, 3, 2, 4], [4, 5, 6, 7])


pl.figure(3)
#PLOTTING IN SAME GRAPH
pl.plot([1, 2, 3, 4, 5, 6, 7, 8], [5, 6, 5, 4, 6, 4, 5, 7])
#PLOTTING IN SAME GRAPH
pl.plot([1, 2, 3, 4, 5, 6, 7, 8], [5, 6, 7, 9, 9, 5, 7, 6])
