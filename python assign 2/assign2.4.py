"""
4. Write a python program to find the greatest of three numbers entered by the
user.
"""
#input 3 numbers
n1 = int(input("Enter the first number\n"))
n2 = int(input("Enter the second number\n"))
n3 = int(input("Enter the third number\n"))

#check if n1 is greater than n2 and similarly ahead for the same
if n1>n2:
    if n1>n3:
        print("The greatest of three numbers is", n1)
    else:
        print("The greatest of three numbers is", n3)
elif n1<n2:
    if n2>n3:
        print("The greatest of three numbers is", n2)
    else:
        print("The greatest of three numbers is", n3)