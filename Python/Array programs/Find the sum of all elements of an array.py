def sum1(arr):
    result =0
    for x in arr:
        result +=x
    return result

def sum2(arr):
    result = sum(arr)
    return result 

if __name__ == "__main__":
    arr = [10,20,30,40,50]
    print('Sum 1 : {}'.format (sum1(arr)))
    print('Sum 2 : {}'.format (sum2(arr)))