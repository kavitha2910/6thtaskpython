def is_happy_number(n):
    seen = set()
    while n != 1 and n not in seen:
        seen.add(n)
        n = sum(int(i)**2 for i in str(n))
    return n == 1

def count_happy_numbers(numbers):
    count = 0
    for num in numbers:
        if is_happy_number(num):
            count += 1
    return count

given_list = [10, 501, 22, 37, 100, 999, 87, 351]

happy_count = count_happy_numbers(given_list)

print("Count of happy numbers:", happy_count)

