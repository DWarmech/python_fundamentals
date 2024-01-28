import sys

quantity = int(input())

max_value = -sys.maxsize
max_weight = -sys.maxsize
max_time = -sys.maxsize
max_quality = -sys.maxsize

for snowball in range(quantity):
    max_found = False
    weight = int(input())
    needed_time = int(input())
    quality = int(input())

    snowball_value = (weight / needed_time) ** quality

    if max_weight < weight:
        max_weight = weight
    if max_time < needed_time:
        max_time = needed_time
    if max_quality < quality:
        max_quality = quality

    if max_value < snowball_value:
        max_value = snowball_value
        max_found = True

    if max_found:
        print(f"{max_weight} : {max_time} = {int(max_value)} ({max_quality})")
        max_Found = False
    else:
        continue
