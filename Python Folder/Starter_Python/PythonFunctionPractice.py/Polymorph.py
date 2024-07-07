def PolyFunc(num1, num2):
    return num1*num2


num1 = input("Enter first number = ")
if num1 >= 'a' or num1 >= 'A':
    num1 = num1
else:
    num1 = int(num1)

num2 = input("Enter second number = ")
if num2 >= 'a' or num2 >= 'A':
    num2 = num2
else:
    num2 = int(num2)

result = PolyFunc(num1, num2)
print(f"Multiply is = {result}")
