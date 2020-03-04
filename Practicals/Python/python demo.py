import random 
bins={}
for i in range (1,11):
    bins [i]=0
for i in range (1,101):
    r= random.randint(1,10)
    bins[r]=bins[r]+1
print(bins)
def mbin():
    max_=0
    max_i=-1
    for each in bins :
        if (bins[each]>max_):
            max_i=each
            max_=bins[each]
    print(max_i)
    return max_i

while (len(bins)>0):
    b=mbin()
    del(bins[b])
