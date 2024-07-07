num = int(input("Enter a Number = "))
i = 2
mid = num/2

while i <= mid:
    if num % i == 0:
        print(f"{num} is not a prime number")
        exit()
    i += 1

print(f"{num} is prime number")
