def hanoi(x):
    if x ==1:
        return 1 
    else :
        return 2*hanoi(x-1)+1
        
x = int(input ("ENter the number of disks :"))
print ('Number of steps :',hanoi(x))