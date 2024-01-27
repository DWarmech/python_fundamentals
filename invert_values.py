import math

numbers = input()
new = []
old = []
numbers_in_list = numbers.split()

for number in numbers_in_list[0:]:

    compare_number = numbers_in_list[0]
    compare_number = int(compare_number)

    if compare_number >= 0:
        negative_number = 0 - compare_number
        new.append(negative_number)
        del numbers_in_list[0]
    elif compare_number < 0:
        positive_number = abs(compare_number)
        new.append(positive_number)
        del numbers_in_list[0]

print(new)
