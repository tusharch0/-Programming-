amt = int (input ("Enter sales amount : "))

if (amt >0):
    if amt <=5000:
        disc =amt *0.05
    else :
        if amt <=15000:
            disc=amt *0.12
        else:
            if amt <=25000:
                disc =0.2*amt 
            else:
                disc =0.3*amt 

    print ("Discount : ",disc ) 
    print ("Net pay : ",amt-disc )
else :
    print("Invalid Amount")