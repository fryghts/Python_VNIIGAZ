numbers = input().split(',')
num_count = [0 for i in range(len(numbers))]
while (s := input()) != '.':
    for i in range(len(numbers)):
        num_count[i] += s.count(numbers[i])

print(numbers, num_count)
