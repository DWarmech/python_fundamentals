num = int(input())
word = input()


for number in range(num):
    counter = 0
    isPure = True
    while isPure != 0 and counter < len(word):
        char = word[counter]
        isPure = not (char == ',' or char == '.' or char == '_')
        counter += 1

    if isPure:
        print(f"{word} is pure.")
        word = input()
    else:
        print(f"{word} is not pure!")
        word = input()
