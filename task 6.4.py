def sum_first_last_digit(number):
    num_str = str(number)
    first_digit = int(num_str[0])
    last_digit = int(num_str[-1])
    
    sum_result = first_digit + last_digit
    
    return sum_result

num = int(input("Enter an integer: "))
result = sum_first_last_digit(num)
print(f"The sum of the first and last digit of {num} is: {result}")