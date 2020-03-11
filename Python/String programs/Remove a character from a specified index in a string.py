def remove_char(str, n):
    front = str[:n]  # up to but not including n
    back = str[n + 1:]  # n+1 till the end of string
    return front + back


print(remove_char('HelloWorld', 3))
print(remove_char('Hello', 4))
print(remove_char('Website', 1))
