# My first calculation
print("3*2 = ")
print(3*2)

# My first variable
x = 3*2
print("Variable x = " + str(x))

# Re-using the value of a variable
x = x*10
print("x is now = " +str(x))

# A basic calculator

# Get first value
a = int(input("Enter the first number: "))

# Get the operator (+ - * /)
op = input("Indicate operation + - * /: ")

# Get second value
b = int(input("Enter the second number: "))

if op == "+":
    c = a+b
elif op == "-":
    c = a-b
elif op == "*":
    c = a*b
else:
    c = a/b

print(int(c))