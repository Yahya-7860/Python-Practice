age = int(input("Enter age : "))
day = input("Enter Day : ")

price = 12 if age >= 18 else 8

if day == "wednesday":
    price -= 2
    print(
        f'Wednesday Offer Applied with $2 discount, actual price was ${price+2}')

print(f'Price to pay : ${price}')
