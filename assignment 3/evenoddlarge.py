def EvenOdd(n):
    if n % 2 == 0:
        print("The number is Even")
    else:
        print("The number is Odd")

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % 2 == 0:
            return False
    return True

def find_largest(a, b, c):
    if a >= b and a >= c:
        return a
    elif b >= a and b >= c:
        return b
    else:
        return c

n = int(input("Enter the number: "))
EvenOdd(n)

if is_prime(n):
    print("The number is Prime")
else:
    print("The number is not Prime")
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
num3 = int(input("Enter the third number: "))

largest = find_largest(num1, num2, num3)
print("The largest number is:", largest)
