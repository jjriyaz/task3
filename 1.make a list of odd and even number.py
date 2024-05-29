##make a list of odd and even number

def separate(numbers):
    even_numbers = []
    odd_numbers = []
    
    for num in numbers:
        if num % 2 == 0:
            even_numbers.append(num)
        else:
            odd_numbers.append(num)
    
    return even_numbers, odd_numbers

# Given list
numbers = [10, 501, 22, 37, 100, 999, 87, 351]

# Separate even and odd numbers
even_nums, odd_nums = separate(numbers)

print("Even numbers:", even_nums)
print("Odd numbers:", odd_nums)
