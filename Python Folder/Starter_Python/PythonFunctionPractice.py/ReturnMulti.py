import math

def AreaCircumOfCircle(r):
    area = round(math.pi*(r**2), 2)
    circum = round(2*math.pi*r, 2)
    return area, circum


r = int(input("Enter radius = "))
(area, circum) = AreaCircumOfCircle(r)

print(f"Area is {area} and circum is {circum}")
