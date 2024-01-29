word = input()

while word != "Welcome!":
    
    if word == "Voldemort":
        print(f"You must not speak of that name!")
        break

    if len(word) < 5:
        print(f"{word} goes to Gryffindor.")
    elif len(word) == 5:
        print(f"{word} goes to Slytherin.")
    elif len(word) == 6:
        print(f"{word} Ravenclaw.")
    elif len(word) > 6:
        print(f"{word} goes to Hufflepuff.")

    word = input()

if word != "Voldemort":
    print(f"Welcome to Hogwarts.")

