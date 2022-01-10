"""
Write a python program to store different data type values into a list. (For an
example: Student [SID, Name, Gender, Course Name, CGPA]).
Note: Use Gender values: ‘F’, ‘M’, ‘U’ (For Unknown).
CGPA should have floating type values (example: 7.5).
"""
# so firstly as usual taking input from  user about sid,name,etc.
print("Hi, PEC welcomes you first yearties\n", "We are arranging your data for further use, so kindly enter your details as mentioned.")
print("Enter your SID (as per provided by pec) eg. {21103052}")
inpnum1 = int(input())
print("Enter your full name")
inpnum2 = str(input())
inpnum3 = inpnum2.capitalize()
print("Choose your gender as regards:\n", "M:Male\n", "F:Female\n", "U:Unknown")
inpnum4 = str(input())
inpnum5 = inpnum4.capitalize()
print("Choose your course name:\n", "CHEM:1, MATHS:2, INTRODUCTION TO COMPUTING:3, IEEE:4, ED:5")
inpnum6 = int(input())
print("Enter your CGPA (eg. 9.0, 8.5, 6.7)")
inpnum7 = float(input())

# so we have taken all the data and stroed it in {inpnum_}
list1 = [inpnum1, inpnum3,inpnum5,inpnum6,inpnum7,]
print(list1)

print("THANKS ", inpnum3)
print("Your data has been recorded and now can be used for further purposes\n", "Have fun!!")