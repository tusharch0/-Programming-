import sys 
def push (element,size,stack):
    global top
    if top >=size-1:
        print('Stack overflow')
        sys.exit()
    else :
        top +=1
        stack[top] = element 