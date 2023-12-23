
list1 = [1,2,3,4,5]
list2 = [8,7,5,3,1]
list3 = [6,7,5,1,9,]

duplicates = []
for num in list1:
    if num in list2 and num in list3 and num not in duplicates:
        duplicates.append(num)
if duplicates:
    print("Duplicates found among the three lists:", duplicates)
else:
    print("No duplicates found among the three lists.")