string = input("Enter a string = ")

newstring = ''

print("Before= " + string)

for i in string:
    newstring = i+newstring

print(f"After = {newstring}")
