def stdv (X):
    mean = sum(X)/len(X)
    tot = 0.0
    for x in X:
        tot = tot +(x- mean )**2
    return(tot /len(X))**0.5

sample = [1,2,3,4,5]
print ("Standard Deviation of the sample is : ",stdv(sample))
sample = [1,2,3,-4,-5]
print ("Standard Deviation of the sample is : ",stdv(sample))
sample = [10,-20,30,-40,50]
print ("Standard Deviation of the sample is : ",stdv(sample))
