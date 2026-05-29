# -*- coding: utf-8 -*-

#Q1 Assign a variable to hold your age and print it.
a = int(input("Enter your age"))
print(a)

#Q2 Create a variable that holds your name as a string and print it.
b = input("Enter your name")
print(a)

#Q3  Write a program that assigns two numbers to variables and prints their sum.
c = int(input("Enter first number"))
d = int(input("Enter second number"))
print(c+d)

#Q4 Create a variable to hold your weight as a float and print it.
a = float(input("Enter your weight"))
print(a)

#Q5 Create a variable x with an integer value and y with a string value. Concatenate them in a print statement (without changing their types).
x = int(input("Enter first number "))
y = input("Enter second number ")
print(x,y)

#Q6 Write a program that assigns a value to a boolean variable (True or False) and prints its value.
 a = bool(input("Enter first number "))
 print(a)

#Q7 Assign an integer value to a variable and a float value to another, then perform a division and print the result.
x = int(input("Enter first number "))
y = float(input("Enter second number "))
print(x/y)

#Q8  Create a list of integers and assign it to a variable. Print the first and last item of the list.
a = [1,2,3,4]
print(a[0])
print(a[3])

#Q9 Assign a string value to a variable and print the string in uppercase letters.
a = input("Enter first number ")
print(a.upper())

#Q10 Write a program that assigns a number to a variable and checks if it is greater than 10, printing True if it is, False otherwise.
a = int(input("Enter first number "))
if a>10:
    print("True")
else:
    print("False")

#Q11  Write a program that assigns two numbers to variables, multiplies them, and prints the result.
a = int(input("Enter first number "))
b = int(input("Enter second number "))
print(a*b)

#Q12 Create a variable num with a string value that represents an integer. Convert the string to an integer and print the result.
num = input("Enter first number ")
print(int(num))

#Q13 Create a list with 5 elements. Change the value of the second element to a new value and print the updated list.
a = [1,2,4,5,6]
a[1]=3
print(a)

#Q14  Create a variable that holds a floating point number and check if it is an integer using a conditional statement.
a = float(input("Enter first number "))
if a==int(a):
    print("True")
else:
    print("False")

#Q15 Write a program that assigns a value to a variable and prints its type using the type() function.
a = int(input("Enter a no."))
print(type(a))

#Q16 Create a list of strings. Add a new string to the list and print the updated list.
a = [1,2,3,4]
a.append(5)
print(a)

#Q17 Write a program that assigns values to two variables, then swaps the values of the two variables and prints the result.
a = int(input("Enter first number "))
b = int(input("Enter second number "))
a,b=b,a
print(a,b)

#Q18 Create a program that takes two variables as input (using input()), converts them to integers, and prints their sum.
a = (input("Enter first number "))
b = (input("Enter second number "))
print(int(a)+int(b))

#Q19  Write a program that assigns a float to a variable and rounds it to the nearest integer using the round() function. Print the result.
a = float(input("Enter first number "))
print(round(a))

#Q20 Create a program that assigns a string to a variable. Use string slicing to extract and print the first 3 characters of the string.
a = input("Enter first number ")
print(a[0:3])
