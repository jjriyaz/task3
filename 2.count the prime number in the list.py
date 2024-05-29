##count the prime number in the list

def is_prime(num):
    if num <= 1:
        return False
    elif num == 2:
        return True
    elif num % 2 == 0:
        return False
    else:
        for i in range(3, int(num ** 0.5) + 1, 2):
            if num % i == 0:
                return False
        return True

def get_primes(numbers):
    prime_numbers = []
    prime_count = 0
    for num in numbers:
        if is_prime(num):
            prime_numbers.append(num)
            prime_count += 1
    return prime_count, prime_numbers

# Given list
numbers = [10, 501, 22, 37, 100, 999, 87, 351]

# Get prime numbers and count
prime_count, prime_nums = get_primes(numbers)

# Print the results
print("Count of prime numbers:", prime_count)
print("Prime numbers:", prime_nums)
