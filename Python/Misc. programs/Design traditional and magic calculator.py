import re

print("Our Magical Calculator")
print("Type x to close")

previous = 0
run = True


def performMath():
    global run
    global previous
    equation = ""
    if previous == 0:
        equation = input("Enter Equation: ")
    else:
        equation = input(str(previous))

    if equation == 'x':
        print("GoodBye!!!")
        exit(0)
    else:
        equation = re.sub('[a-zA-Z,:()" "]', "", equation)

    if previous == 0:
        previous = eval(equation)
    else:
        previous = eval(str(previous) + equation)


while run:
    performMath()
