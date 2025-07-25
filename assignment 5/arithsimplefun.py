a = int(input("Enter the first number = "))
b = int(input("Enter the second number = "))

def add():
    c = a + b
    print("Addition of a and b is ",c)
add()

def sub():
    c = a - b
    print("Substraction of a and b is ",c)
sub()

def mul():
    c = a * b
    print("Multiplication of a and b is ",c)
mul()

def div():
    c = a / b
    print("Division of a and b is ",c)
div()

def mod():
    c = a % b
    print("Modulus of a and b is ",c)
mod()

def Flr():
    c = a // b
    print("Floor Divison of a and b is ",c)
Flr()

def Ex():
    c = a ** b
    print("Exponentation of a and b is ",c)
Ex()



num1 = int(input("Enter the number "))
num2 = int(input("Enter the number "))

def add(num1: int, num2: int) -> int:
    num3 = num1 + num2
    return num3
def sub(num1: int, num2: int) -> int:
    num3 = num1 - num2
    return num3
def mul(num1: int, num2: int) -> int:
    num3 = num1 * num2
    return num3
def div(num1: int, num2: int) -> float:
    num3 = num1 / num2
    return num3
def mod(num1: int, num2: int) -> int:
    num3 = num1 % num2
    return num3
def exp(num1: int, num2: int) -> int:
    num3 = num1 ** num2
    return num3
def flr(num1: int, num2: int) -> int:
    num3 = num1 // num2
    return num3


ans = add(num1, num2)
print(f"The addition of {num1} and {num2} results {ans}.")


ans = sub(num1, num2)
print(f"The Substraction of {num1} and {num2} results {ans}.")


ans = mul(num1, num2)
print(f"The Multiplication of {num1} and {num2} results {ans}.")


ans = div(num1, num2)
print(f"The Division of {num1} and {num2} results {ans}.")


ans = mod(num1, num2)
print(f"The Modulus of {num1} and {num2} results {ans}.")


ans = exp(num1, num2)
print(f"The Modulus of {num1} and {num2} results {ans}.")


ans = flr(num1, num2)
print(f"The Modulus of {num1} and {num2} results {ans}.")

