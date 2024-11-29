# A Calculator With Functions

# Get first value
def get_first_value():
    a = int(input("Enter the first number: "))
    return a

# Get the operator (+ - * /)
def get_operator():
    op = input("Indicate operation + - * /: ")
    return op

# Get second value
def get_second_value():
    b = int(input("Enter the second number: "))
    return b

# Calculate Answer

v1 = get_first_value()
vo = get_operator()
v2 = get_second_value()

# Select operator

if vo == "+":
    result = v1+v2
elif op == "-":
    result = v1-v2
elif op == "*":
    result = v1*v2
elif op == "/":
    result = v1/v2
else:
    result = "Invalid Operator!"

print(result)