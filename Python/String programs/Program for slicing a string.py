def slice(str ,n):
    if len(str)<n:
        n=len(str )
    front = str [:n] 
    return front 

print(slice ("Chocolate",5))
print(slice ("hello_world",6))
print(slice ("Hello",10))
