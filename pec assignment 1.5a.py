"""
5. List: color ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']
a. Write a Python program to print a specified list after removing 4th element.
Expected output: color [Red', 'Green', 'White', 'Pink', 'Yellow']
b. Remove ‘Black’ and ‘Pink’ from the list and replace them with ‘Purple’.
Do that in one line code.
"""
#first we are making a list asked.
List1 = ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']
#5a
# now i am removing the black color from list
List1.pop(3)
print(List1)

