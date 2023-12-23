def sublist_with_zero_sum(nums):
    sum_set = set()
    current_sum = 0

    for num in nums:
        current_sum += num
        if current_sum == 0 or current_sum in sum_set:
            return True

        sum_set.add(current_sum)
    return False
given_list = [4, 2, -3, 1, 6]
result = sublist_with_zero_sum(given_list)

if result:
    print("There exists a sublist with sum zero.")
else:
    print("There is no sublist with sum zero.")
