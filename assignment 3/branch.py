# Input: Taking a number from the user
number = int(input("Enter a number: "))

# Branching statements
if number > 0:
    print(f"{number} is a positive number.")
elif number < 0:
    print(f"{number} is a negative number.")
else:
    print("The number is zero.")

# Nested if statement example
print("\nNested if example:")
if number != 0:
    if number % 2 == 0:
        print(f"{number} is an even number.")
    else:
        print(f"{number} is an odd number.")
else:
    print("Zero is neither odd nor even.")
