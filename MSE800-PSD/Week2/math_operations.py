import math

def operations(a,b):
    return {"Sum ": a+b, "Difference":a-b, "Multiplication":a*b}

def division(a,b):
    return {"Quotient":a//b, "Remained":a%b}

def factorial(a):
    return math.factorial(int(a))

def greater_num(a,b):
    return max(a,b)

a=float(input("Enter first number (a):"))
b=float(input("Enter second number (b):"))

print("\nOutput:")
print(operations(a,b))
print(division(a,b))
print(f"factorial of 'a' {a} is: {factorial(a)}")
print(f"The greater number of the two is : {greater_num(a,b)}")

def add_complex(z1, z2):
    return z1 + z2

def multiply_complex(z1, z2):
    return z1 * z2

a = float(input("Enter real part of first number: "))
b = float(input("Enter imaginary part of first number: "))
c = float(input("Enter real part of second number: "))
d = float(input("Enter imaginary part of second number: "))

z1 = complex(a, b)
z2 = complex(c, d)
print(f"\nNumber 1: {z1}")
print(f"Number 2: {z2}")
print(f"Sum: {add_complex(z1, z2)}")
print(f"Product: {multiply_complex(z1, z2)}")