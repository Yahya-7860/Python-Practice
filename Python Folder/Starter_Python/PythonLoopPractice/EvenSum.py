# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

numbers = []

for x in range(10):
    ele = int(input(f"Enter Number {x} = "))
    numbers.append(ele)

Sum = 0

for x in numbers:
    if x % 2 == 0:
        Sum += x

print(f'Even Sum = {Sum}')
