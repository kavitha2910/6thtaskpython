def first_non_repeating_element(nums):
    frequency = {}
    
    # Count frequency of each number in the list
    for num in nums:
        if num in frequency:
            frequency[num] += 1
        else:
            frequency[num] = 1
    
    # Find the first non-repeating element
    for num in nums:
        if frequency[num] == 1:
            return num
    return None
numbers = [1,2,3,4,5,4,3,2,1]
result = first_non_repeating_element(numbers)

if result is not None:
    print(f"The first non-repeating element is: {result}")
else:
    print("No non-repeating element found in the list.")