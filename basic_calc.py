# A basic calculator

# Get first value
a = int(input("Enter the first number: "))

# Get the operator (+ - * /)
op = input("Indicate operation + - * /: ")

# Get second value
b = int(input("Enter the second number: "))

validops =["+","-","*","/"]

if op == "+":
    c = a+b
elif op == "-":
    c = a-b
elif op == "*":
    c = a*b
elif op == "/":
    c = a/b
else:
    c = "Invalid Operator!"

print(c)