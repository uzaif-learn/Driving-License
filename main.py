print("Welcome to the driving license Verification.\n")

name = input("What is your name? ")
age = int(input("Enter your age: "))

if age >= 18:
    print(f"Dear {name} You are eligible to take the driving test, As you are {age} years old")
else:
    print(f"Hard luck You can come back after {18-age} years!!")