def greeting (str ):
    if len (str )>=5 and str [:5]=='Hello':
        return str 
    return 'Hello ' +str

print(greeting('Tushar '))
print(greeting("Abhi "))  