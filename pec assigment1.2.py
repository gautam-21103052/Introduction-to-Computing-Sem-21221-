"""
Write a python program to compute a person's income tax. Assume following
tax laws:
• All taxpayers are charged a flat tax rate of 20%.
• All taxpayers are allowed a $10,000 standard deduction.
• For each dependent, a taxpayer is allowed an additional $3,000 deduction.
• Gross income must be entered to the nearest penny.
Gross Income and the number of dependents must be asked from the user.
Hint:
Taxable income = Gross Income - Standard deduction - (Dependent deduction
* No. of dependents)
Tax = Taxable Income * Tax Rate
"""

# so firstly we have to take the input from the user about gross income and the number of dependments and convert it into integer
n1 = int(input("Enter your GROSS INCOME(in$) {Remember it should be to the nearest penny}\n"))
n2 = int(input("Enter your number of dependents\n"))
# so now we have to print the users taxable income and tax, by calculating using hints.

n3 = n1-10000-(3000*n2)
n4 = n3*(0.2)
print("Okay so your taxable income is:\n", n3)
print("And your payable tax is:\n", n4)
# so my program is ready try it and its working.


