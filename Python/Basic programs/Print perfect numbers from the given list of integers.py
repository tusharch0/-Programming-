def checkPerfactNum(n):
    i = 2
    sum =1
    while (i<=n//2):
        if (n %i ==0):
            sum +=i
        i += 1
        if sum ==n:
            print (n,end=' ')

if __name__ =="__main__":
    print("Enter list of integer :")
    list_of_integers = list (map(int,input().split()))
    print("Given list of integers: ",list_of_integers)
    print ("Perfect number present in the list is : ")
    for num in list_of_integers:
       checkPerfactNum(num)