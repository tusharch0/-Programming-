def variance(X):
    mean = sum(X)/len(X)
    tot = 0.0
    for x in X:
        tot = tot +(x-mean)**2
    return tot/len(X)

sample =[1,2,3,4,5]
print("variable of the sanple is :",variance (sample))
sample =[1,2,3,4,-4,-5]
print ("varience of the sample is : ",variance(sample))
sample =[10,-20,30,-40,50]
print("variance of the sample is :",variance(sample) )