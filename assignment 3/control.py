# Input: Taking a number from the user
number = int(input("Enter a number: "))

# if-elif-else control statement
if number > 0:
    print(f"{number} is positive.")
elif number < 0:
    print(f"{number} is negative.")
else:
    print("The number is zero.")

# for loop to iterate over a range
print("\nUsing a for loop:")
for i in range(1, 6):  # Iterates from 1 to 5
    print(f"Square of {i} is {i**2}")

# while loop
print("\nUsing a while loop:")
count = 1
while count <= 5:
    print(f"Count is: {count}")
    count += 1  # Increment the count

# break and continue
print("\nUsing break and continue:")
for i in range(1, 10):
    if i == 5:
        print("Breaking the loop at 5.")
        break  # Exits the loop
    elif i % 2 == 0:
        print(f"Skipping even number: {i}")
        continue  # Skips the current iteration
    print(f"Processing number: {i}")
