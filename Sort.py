def sort_numbers(num1,num2,num3):
    number=[num1,num2,num3]
    return sorted(number)

x = int(input("Enter first number: "))
y = int(input("Enter second number: "))
z = int(input("Enter third number: "))
a, b, c = sort_numbers(x, y, z)
print("Original numbers: ", x, y, z)
print("Sorted numbers: ", a, b, c)

