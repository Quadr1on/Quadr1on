number = eval(input("Enter number to convert to binary:\n"))
c = f"{number:b}"
# print(type(c))
if c[-1] == '0':
    print('then number is even')
else:
    print('then number is odd')