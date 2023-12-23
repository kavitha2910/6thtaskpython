
def find_triplet_with_sum(arr, target):
    n = len(arr)
    arr.sort()

    for i in range(n - 2):
        left = i + 1
        right = n - 1

        while left < right:
            current_sum = arr[i] + arr[left] + arr[right]

            if current_sum == target:
                return [arr[i], arr[left], arr[right]]
            elif current_sum < target:
                left += 1
            else:
                right -= 1

    return None

given_list = [10, 20, 30, 9]
target_value = 59

triplet = find_triplet_with_sum(given_list, target_value)

if triplet:
    print(f"The triplet with sum {target_value} is: {triplet}")
else:
    print("No triplet found with the given sum.")