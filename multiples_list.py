factor = int(input())
count = int(input())
count_list = []
counter = 0
compare = 0

while counter < count:
    compare += 1
    if compare % factor == 0:
        count_list.append(compare)
        counter += 1
print(count_list)
