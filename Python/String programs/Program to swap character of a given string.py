def swap_string(str):
    if len(str) <= 1:
        return str

    mid = str[1:len(str) - 1]
    return str[len(str) - 1] + mid + str[0]


print(swap_string('Hello World'))
print(swap_string('Hello'))
print(swap_string('G'))
print(swap_string('I love my India!'))
