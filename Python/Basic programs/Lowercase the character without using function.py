st = input ('Type a string : ')
out = ''
for n in st:
    if n not in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ':
        out = out +n 
    else :
        k =ord (n)
        l = k+32
        out = out + chr(l)
print('------>',out )
 