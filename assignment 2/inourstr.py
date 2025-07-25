# Input: Taking a user's name
name = input("Enter your name: ")

# Input: Taking a user's age
age = int(input("Enter your age: "))

# String concatenation
greeting = "Hello, " + name + "!"

# String formatting
info = f"You are {age} years old."

# Output: Printing the results
print(greeting)
print(info)

# String operations
uppercase_name = name.upper()  # Convert to uppercase
lowercase_name = name.lower()  # Convert to lowercase
reversed_name = name[::-1]     # Reverse the string

# Output: Displaying string operations
print("Your name in uppercase:", uppercase_name)
print("Your name in lowercase:", lowercase_name)
print("Your name reversed:", reversed_name)
