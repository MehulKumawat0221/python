#Q1
a = int(input("Enter your age"))
if a>=18:
    print("You are eligible for vote")
else:
    print("You are not eligible for vote")

#Q2
a =int(input("Enter the amount"))
if a>100:
  a = a*0.1
    print("totle bill ", a)
else:
    print("Totle bill ",a)

#Q3
a = int(input("Enter your age"))
if a<=12:
  a = 7
    print("ticket price is ",a)
elif a>=12 and a<=60:
  a = 10
    print("ticket price is ",a)
elif a>60:
  a = 8
    print("ticket price is ",a)
else
    print("Error")

#Q4
a =int(input("Enter your income"))
b = int(input("Enter your cedit score"))
if a >50000 and b>650:
  print("loan is approved")
else:
    print("loan is not approved")

#Q5
a = int(input("Enter how many days you will come to gym in a week"))
if a <= 3:
  print("you should take bronze plane")
elif a >3 and a<=5:
  print("you should take silver plane")
elif a>5:
  print("you should take gold plane")
else:
  print("error")

#Q6
a =int(input("Enter your bill amount"))
b =input("Enter your location in side of the city or outside")
c= int(input("Enter to distance in km also"))
if a>50 and b =="inside":
  print("tootle bill ",a)
elif a <50 and b =="inside":
  a = a+5
  print("tootle bill ",a)
elif b == "outside":
  b = b - 50
  b = b*5
  a = a+b
  print("tootle bill ",a)
else:
  print("error")

#Q7
a = int(input("Enter your time in hour"))
b = 5
c = 3
if a <=2:
  print("your bill is ",b)
elif a>2:
  a = b + a*c
  print("your bill is ",a)

#Q8
a = int(input("Enter your units"))
if a<=100:
  a = a*0.1
  print("your bill is ",a)
elif a>100 and a<=200:
  a = a*0.15
  print("your bill is ",a)
elif a >200:
  a = a*0.2
  print("your bill is ",a)
else:
  print("error")

#Q9
a =int(input("Enter your marks"))
if a >=90:
  print("A grade")
elif a>80 and a<=89:
  print("B grade")
elif a>70 and a<=79:
  print("C grade")
elif a>60 and a<= 69:
  print("d grade")
elif a<60:
  print("grade f")

#Q10
a= int(input("Enter your bags weight"))
b=10
if a<=15:
  print("free baggage allowanc")
elif a>15:
  a = a*b
  print("your baggage charge is ",a)
else:
  print("Error")

