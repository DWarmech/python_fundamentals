n = int(input())
positives = []
negatives = []
positives_counter = 0
negatives_sum = 0

for number in range(n):
    num = int(input())
    if num >= 0:
        positives.append(num)
        positives_counter += 1
    elif num < 0:
        negatives.append(num)
        negatives_sum += num

print(positives)
print(negatives)
print(f"Count of positives: {positives_counter}")
print(f"Sum of negatives: {negatives_sum}")
