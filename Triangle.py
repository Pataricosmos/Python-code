a=float(input("Enter first side:"))
b=float(input("Enter second side:"))
c=float(input("Enter thirs side:"))
r = False
if a>b and a>c:
    r=(b+c) > a
elif b>a and b>c:
    r=(a+c) > c
else:
    r = (a+b) > c
if r == True:
    print("Sides will foram a triangle")
else:
    print("Sides will not form a triangle")
