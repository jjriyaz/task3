def find_minimum_element(sorted_list):
    
    # If the list is empty, return None
    if not sorted_list:
        return None
    
    # Minimum element is the first element in a sorted list
    return sorted_list[0]

# Test the function with an example sorted list
sorted_list = [1, 2, 3, 4, 5]
min_element = find_minimum_element(sorted_list)
print("Minimum element in the sorted list:", min_element)