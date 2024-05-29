def first_non_repeating_element(nums):
    # Create a dictionary to store the frequency of each element
    frequency = {}
    
    # Iterate through the list to count the frequency of each element
    for num in nums:
        if num in frequency:
            frequency[num] += 1
        else:
            frequency[num] = 1
    
    # Iterate through the list again to find the first non-repeating element
    for num in nums:
        if frequency[num] == 1:
            return num
    
    # If no non-repeating element is found, return None
    return None

# Test the function with an example list
nums = [4, 6, 2, 3, 9, 4, 3, 6]
result = first_non_repeating_element(nums)
if result is not None:
    print("First non-repeating element:", result)
else:
    print("No non-repeating element found in the list.")
