num = int(input('Enter Number = '))
i = 1
ans = 1

while i <= num:
    ans *= i
    i += 1

print(f'Factorial of {num} is : {ans}')
