number = int(input())
even = []
odd = []
negative = []
positive = []

for i in range(number + 1):
    command = input()

    if command == "even":
        print(even)
        break
    elif command == "odd":
        print(odd)
        break
    elif command == "negative":
        print(negative)
        break
    elif command == "positive":
        print(positive)
        break

    command = int(command)

    if command % 2 == 0:
        even.append(command)
    elif command % 2 == 1:
        odd.append(command)

    if command >= 0:
        positive.append(command)
    elif command < 0:
        negative.append(command)
