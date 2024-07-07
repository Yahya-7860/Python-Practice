password = input("Enter Password : ")

pas_len = len(password)
pas_strength = ''

if (pas_len < 6):
    pas_strength = "Weak Password"
elif pas_len < 10:
    pas_strength = "Medium Password"
else:
    pas_strength = "Very Strong Password"

print(f"Password Strength : {pas_strength}")
