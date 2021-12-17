def get_min_numbers(numbers):
    numbers=sorted(numbers)
    return numbers[0]

numbers=[34,12,5,45,8]
min_number = get_min_numbers(numbers)
print("Min number: ", min_number)