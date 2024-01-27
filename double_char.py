word = input()

while word != "End":
    if word == "SoftUni":
        word = input()
        continue
    for char in word:
        repeat = char + char
        print(repeat, end="")
    print()
    word = input()
