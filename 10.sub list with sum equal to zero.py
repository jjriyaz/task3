def has_sublist_with_zero_sum(nums):
    prefix_sum = 0
    sum_set = set()
    
    for num in nums:
        prefix_sum += num
        
        # If prefix sum becomes zero or repeats, there is a sublist with sum equal to zero
        if prefix_sum == 0 or prefix_sum in sum_set:
            return True
        
        # Add the current prefix sum to the set
        sum_set.add(prefix_sum)
    
    return False

# Test the function with the given list
nums = [4, 2, -3, 1, 6]
if has_sublist_with_zero_sum(nums):
    print("There is a sublist with sum equal to zero.")
else:
    print("There is no sublist with sum equal to zero.")
