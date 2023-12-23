def find_min_element(sorted_list):
    if not sorted_list:
        return None 
    return sorted_list[0]

ratings = [2, 3, 4, 5, 6]
min_rating = find_min_element(ratings)

if min_rating is not None:
    print(f"The minimum element in the list is: {min_rating}")
else:
    print("The list is empty.")