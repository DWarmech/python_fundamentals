number = int(input())
given_word = input()
phrase = []

for word in range(number):
    new_word = input()
    phrase.append(new_word)

print(phrase)

for i in range(len(phrase) - 1, -1, -1):
    element = phrase[i]
    if given_word not in element:
        phrase.remove(element)

print(phrase)
