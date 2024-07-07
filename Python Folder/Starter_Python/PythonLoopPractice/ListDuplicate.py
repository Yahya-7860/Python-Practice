items = ["apple", "banana", "mango", "orange", "mango"]

j = 0

for i in items:
    if i in items[j+1:]:
        print(f"Repeated item is : {i}")
        exit()
    else:
        j += 1

print("No repeated item found")