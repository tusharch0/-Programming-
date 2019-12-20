amt =int (input ("Enter sale amount : "))
if (amt >0):
    if amt <=5000:
        disc =amt*0.05
    elif amt <=15000:
        disc =amt *0.12
    elif amt <=25000:
        disc =0.2*amt 
    else:
        disc =0.3*amt 
    
    print("Discount : ",disc )
    print("Net pay : ",amt-disc)
else :
    print ("Invalid Amount ")