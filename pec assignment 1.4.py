"""
4. Write a python program to enter marks of 5 students into a list and display
them in sorted manner.
"""
# so in this program we are not mentioned marks of which subject are taken
# so i am taking mathematics marks and arranging them in descending order

print("We are recording maths marks of students of CSE branch")
print("So, kindly respective students enter your marks as asked")
n1 = int(input("SID:21103001 , Enter you marks\n"))
n2 = int(input("SID:21103002 , Enter you marks\n"))
n3 = int(input("SID:21103003 , Enter you marks\n"))
n4 = int(input("SID:21103004 , Enter you marks\n"))
n5 = int(input("SID:21103005 , Enter you marks\n"))

dict1 = [ ["SID:21103001", n1], ["SID:21103002", n2], ["SID:21103003", n3], ["SID:21103004", n4], ["SID:21103005", n5] ]
for item, marks in dict1:
    print(item,"got", marks, "marks in Maths")

