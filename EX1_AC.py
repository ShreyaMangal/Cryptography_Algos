'''num1 = int(input("Enter first number:"))
num2 = int(input("Enter second number:"))
sum = num1 + num2
print(sum)
#Prefer to convert string to int in try and except block to deal with any tracebacks.'''

# BASIC CALCULATOR
num1 = int(input("Enter first number:"))
num2 = int(input("Enter second number:"))
op = input("Enter operator:")

if op == '+':
    res = num1 + num2
elif op == '-':
    res = num1 - num2
elif op == '/':
    res = num1/num2
elif op == '*':
    res = num1 * num2
else:
    print("Wrong operator!")

print(res)

    

           