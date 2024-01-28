group = int(input())
days = int(input())
coins = 0

for day in range(1, days + 1):
    if day % 10 == 0:
        group -= 2
    if day % 15 == 0:
        group += 5

    if day % 3 == 0:
        coins -= 3 * group
    if day % 5 == 0:
        coins += 20 * group
        if day % 3 == 0:
            coins -= 2 * group

    coins += 50
    coins -= 2 * group

coins_per_companion = coins // group
print(f"{group} companions received {round(coins_per_companion)} coins each.")
