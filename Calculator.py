b=0
c=0

print("1 for square root calculator")
print("2 for addition calculator")
print("3 for subtraction calculator")
print("4 for multiplication calculator")
print("5 for division calculator")
print("6 for percent calculator")
print("7 for Circumference calculator")
print("8 for Area calculator")

a = float(input('Enter what you need: '))

if(a==1):
    num = float(input('Enter a number: '))
    sqrt = num ** 0.5
    print('The square root of %0.3f is %0.3f' % (num, sqrt))
else:
    pass

if(a==2):
     add1 = int(input("Enter first number: "))
     add2 = int(input("Enter second number: "))
     result = add1 + add2
     print(add1," + ",add2," = ",result)
else:
    pass

if(a==3):
     sub1 = int(input("Enter first number: "))
     sub2 = int(input("Enter second number: "))
     result = sub1 - sub2
     print(sub1," - ",sub2," = ",result)

if(a==4):
     mul1 = int(input("Enter first number: "))
     mul2 = int(input("Enter second number: "))
     result = mul1 * mul2
     print(mul1," * ",mul2," = ",result)
else:
    pass

if(a==5):
     div1 = int(input("Enter first number: "))
     div2 = int(input("Enter second number: "))
     result = div1 / div2
     print(div1," / ",div2," = ",result)
else:
    pass

if(a==6):
     per1 = int(input("Percent Number: "))
     per2 = int(input("Enter second number: "))
     per3 = (100)
     result = per1 / per2 * per3
     print(per1," / ",per2," * ",per3," = ",result)
else:
    pass

if(a==7):
    b = float(input('Calculate Circumference through diameter(1) or Radius(2): '))
else:
    pass


if(b==1):
    pi2 = 3.14159265359
    pi3 = int(input("Enter Diameter: "))
    result = pi2 * pi3
    print(pi2," * ",pi3," = ",result)
else:
    pass

if(b==2):
    pi1 = 2
    pi2 = 3.14159265359
    pi3 = int(input("Enter radius: "))
    result = pi1 * pi2 * pi3
    print(pi1," * ",pi2," * ",pi3," = ",result)
else:
    pass


if(a==8):
    c = float(input('Calculate Area of Square/Rectangle(1) or Circle(2): '))
else:
    pass

if(c==1):
    side1 = int(input("First Side: "))
    side2 = int(input("Second Side: "))
    result = side1 * side2
    print(side1," * ",side2," = ",result)
else:
    pass

if(c==2):
    Cir1 = 3.14159265359
    Cir2 = int(input("Enter radius: "))
    Cir3 = int(input("Enter radius again for square: "))
    result = Cir1 * Cir2 * Cir3
    print(Cir1, " * ", Cir2, " * ", Cir3, " = ", result)
else:
    pass

import time
time.sleep(20)

