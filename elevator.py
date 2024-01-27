import math

n = int(input())  # persons
p = int(input())  # capacity

courses = n / p

print(math.ceil(courses))
