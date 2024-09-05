## Problem 1 ##
#Fix the following code so that its output matches
# Sample output:
# --------------------------------------------------
# my name is Tim Tester, I am 20 years old
# 
# my skills are
#  - python (beginner)
#  - java (veteran)
#  - programming (semiprofessional)
#  
# I am looking for a job with a salary of 2000-3000 dollars per month

name = "Tim Tester"
age = 20
skill1 = "python"
level1 = "beginner"
skill2 = "java"
level2 = "veteran"
skill3 = "programming"
level3 = "semiprofessional"
lower = 2000
upper = 3000

print("my name is " + str(name) + ", I am", age, "years old\n")
print("my skills are")
print("- " + str(skill1) + " (" + str(level1) + ')')
print("- " + str(skill2) + " (" + str(level2) + ')')
print("- " + str(skill3) + " (" + str(level3) + ')')
print("\nI am looking for a job with a salary of " + str(lower) + "-" + str(upper) + " dollars per month")





## Problem 2 ##
#Please finish the script so that: 
# - the following output is printed:
# Sample output:
# --------------------------------------------------
# X val: 27
# Y val: 15
#
# 27 + 15 = 42
# 27 - 15 = 12
# 27 * 15 = 405
# 27 / 15 = 1.8
#
# - The program should work correctly even if the values of the variables are changed.

x = int(input("X val: "))
y = int(input("Y val: "))


sum = x+y
difference = x-y
product = x*y
quotient = x/y

print(int(x), "+", int(y), " = ", sum)

