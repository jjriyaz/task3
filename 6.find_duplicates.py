def find_duplicates(list1, list2, list3):
    # Create sets from the lists to remove duplicates
    set1 = set(list1)
    set2 = set(list2)
    set3 = set(list3)
    
    # Find duplicates by taking the intersection of the sets
    duplicates = set1.intersection(set2, set3)
    
    return list(duplicates)

# Test the function with example lists
list1 = [5, 10, 15, 20, 25]
list2 = [10, 20, 30, 40, 50]
list3 = [2, 4, 6, 8, 10]

duplicate_elements = find_duplicates(list1, list2, list3)
print("Duplicates in the three lists:", duplicate_elements)
