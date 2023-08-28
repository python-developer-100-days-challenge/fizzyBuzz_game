# Initialize a variable to store the sum of numbers matching Fizz Buzz conditions
x = 0

# Iterate through numbers from 1 to 100 (inclusive)
for number in range(1, 101):
    # Check if the number is divisible by both 3 and 5
    if number % 3 == 0 and number % 5 == 0:
        x += number
        print(f"Fizz Buzz")
    # Check if the number is divisible by 5
    elif number % 5 == 0:
        x += number
        print("Buzz")
    # Check if the number is divisible by 3
    elif number % 3 == 0:
        x += number
        print("Fizz")
    else:
        # If the number doesn't meet any condition, print the number itself
        print(number)
