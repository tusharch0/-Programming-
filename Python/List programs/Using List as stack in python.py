# Python Example: use list as stack

# Declare a list named as "stack"
stack = [10, 20, 30]
print("stack elements: ")
print(stack)

# push operation
stack.append(40)
stack.append(50)
print("Stack elements after push opration...")
print(stack)

# push operation
print(stack.pop(), " is removed/popped...")
print(stack.pop(), " is removed/popped...")
print(stack.pop(), " is removed/popped...")
print("Stack elements after pop operation...")
print(stack)
