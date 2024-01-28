commands = int(input())
capacity = 255

for i in range(commands):
    liters = int(input())

    if capacity - liters < 0:
        print("Insufficient capacity!")
        continue
    capacity -= liters

print(255 - capacity)
