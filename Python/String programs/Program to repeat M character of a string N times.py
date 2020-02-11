def multi_time (str ,m,n):
    front_len = m
    if front_len > len(str):
        front_len = len(str)
    front = str[:front_len]

    result = ''
    for i in range (n):
        result = result + front 
    return result 

print(multi_time("Hello_world",7,5))
print(multi_time('tushar',4,3))
print(multi_time('Hello',3,7)) 