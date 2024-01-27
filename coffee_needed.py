word = input()
coffee = 0

while word != "END":
    if word == "coding":
        coffee += 1
    elif word == "CODING":
        coffee += 2

    if word == "dog" or word == "cat":
        coffee += 1
    elif word == "DOG" or word == "CAT":
        coffee += 2

    if word == "movie":
        coffee += 1
    elif word == "MOVIE":
        coffee += 2

    word = input()

if coffee > 5:
    print("You need extra sleep")
else:
    print(coffee)
