def sum_first_and_last_digit(n):
    # Convert the integer to a string to easily access digits
    num = str(n)
    
    # Get the first and last digits
    first_digit = int(num[0])
    last_digit = int(num[-1])
    
    # Calculate the sum
    return first_digit + last_digit

# Test the function
integer = int(input("Enter an integer: "))
result = sum_first_and_last_digit(integer)
print("Sum of the first and last digit:", result)
