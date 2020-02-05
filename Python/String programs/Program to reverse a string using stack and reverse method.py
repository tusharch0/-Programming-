import sys 
def push (element,size,stack):
    global top
    if top >=size-1:
        print('Stack overflow')
        sys.exit()
    else :
        top +=1
        stack[top] = element 

def pop():
    global top 
    if top <0:
        print('Stack Underflow')
        sys.exit()
    else:
        element = stack[top]
        print('%s'%element ,end='')
        top -=1

def reverse_by_sort(string):
    string = list(string)
    rev_str =''
    for i in reversed(string):
        rev_str+=i

    return rev_str

if __name__=='__main__':
    size =11
    stack =[0]*size 
    string = 'Hello_world'
    top =-1

    push('H', 11, stack)
    push('e', 11, stack)
    push('l', 11, stack)
    push('l', 11, stack)
    push('o', 11, stack)
    push('_', 11, stack)
    push('w', 11, stack)
    push('o', 11, stack)
    push('r', 11, stack)
    push('l', 11, stack)
    push('d', 11, stack)

    print("Original String = %s"%string )
    print('\nUsing Stack')
    print('Reversed String = ',end='')
    for i in stack:
        pop()
    print('\n\nUsing sort()')
    print('Reverse string = %s'%reverse_by_sort(string))
