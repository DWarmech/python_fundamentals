quantity = int(input())
days_left = int(input())

ornament_set_price = 2
tree_skirt_price = 5
tree_garland_price = 3
tree_lights_price = 15

total_cost = 0
total_spirit = 0

for day in range(1, days_left + 1):

    if day % 11 == 0:
        quantity += 2
    if day % 2 == 0:
        total_cost += ornament_set_price * quantity
        total_spirit += 5
    if day % 3 == 0:
        total_cost += (tree_skirt_price * quantity) + (tree_garland_price * quantity)
        total_spirit += 3 + 10
    if day % 5 == 0:
        total_cost += (tree_lights_price * quantity)
        total_spirit += 17
        if day % 3 == 0:
            total_spirit += 30
    if day % 10 == 0:
        total_spirit -= 20
        total_cost += (ornament_set_price + tree_skirt_price + tree_garland_price + tree_lights_price)

print(f"Total cost: {total_cost}")
print(f"Total spirit: {total_spirit}")
print(quantity)
