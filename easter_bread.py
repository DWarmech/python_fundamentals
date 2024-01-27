budget = float(input())
kg_price = float(input())
milk_percent = 0
total_loaf = 0
loaf_counter = 0
coloured_eggs = 0

pack_eggs = kg_price * 0.75
milk_percent += (kg_price * 0.25)
liter_milk = kg_price + milk_percent
milk_for_bread = 0.25 * liter_milk

loaf_price = pack_eggs + kg_price + milk_for_bread

while budget > 0:
    if budget > loaf_price:
        loaf_counter += 1
        coloured_eggs += 3
        if loaf_counter % 3 == 0:
            lost_eggs = loaf_counter - 2
            coloured_eggs -= lost_eggs
        budget -= loaf_price
    else:
        break

print(f"You made {loaf_counter} loaves of Easter bread! Now you have {coloured_eggs} eggs and {budget:.2f}BGN left.")
