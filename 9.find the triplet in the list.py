def find_triplet(nums, target):
    nums.sort()  # Sort the list to simplify the process
    
    for i in range(len(nums) - 2):
        left = i + 1
        right = len(nums) - 1
        
        while left < right:
            current_sum = nums[i] + nums[left] + nums[right]
            
            if current_sum == target:
                return [nums[i], nums[left], nums[right]]
            elif current_sum < target:
                left += 1
            else:
                right -= 1
    
    return None  # If no triplet is found

# Test the function with the given list and value
nums = [10, 20, 30, 9]
target = 59
triplet = find_triplet(nums, target)

if triplet:
    print("Triplet whose sum is equal to", target, ":", triplet)
else:
    print("No triplet found whose sum is equal to", target)
