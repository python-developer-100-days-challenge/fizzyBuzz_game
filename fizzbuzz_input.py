# Get user input for the range of numbers
start_number = int(input("Enter the starting number: "))
end_number = int(input("Enter the ending number: "))

# Initialize a variable to store the sum of numbers matching Fizz Buzz conditions
x = 0

# Iterate through numbers in the specified range
for number in range(start_number, end_number + 1):
    if number % 3 == 0 and number % 5 == 0:
        x += number
        print(f"Fizz Buzz")
    elif number % 5 == 0:
        x += number
        print("Buzz")
    elif number % 3 == 0:
        x += number
        print("Fizz")
    else:
        print(number)
