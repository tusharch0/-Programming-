def frequency (text):
    text =text.lower()
    dict={}
    for char in text:
        keys = dict.keys()
        if char in keys:
            dict[char]+=1
        else :
            dict [char]=1
    return dict

if __name__ =='__main__':
    user_input =str(input("Enter a string : "))
    print(frequency(user_input))
    user_input =str (input ("Enter another string :"))
    print(frequency(user_input))