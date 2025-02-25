'''There are 2 sisters, Annie and Jane, born in 1996 and 1999 respectively. 
They want to know who was born in a leap year. Write an if-else statement to
determine who was born in a leap year.'''

Annie_birth_year = 1996
Jane_birth_year = 1999

if Annie_birth_year % 4 == 0:
    print("Annie was born in a leap year")
elif Jane_birth_year % 4 == 0:
    print("Jane was born in a leap year")
else:
    print("None of them was born in a leap year")

''' In a school canteen, children under the age of 9 are only given milk porridge 
for breakfast. Children from 10 to 14 are given a sandwich, and children from 
15 to 17 are given a burger. The canteen master asks the age of the student and
gives them breakfast accordingly. Sam's age is 10. Use if-else statement
to determine what the canteen master will offer to him'''

age =10

if age<9:
    print("You get milk porridge for breakfast!")
elif age>9 and age<=14:
    print("You get a sandwich for breakfast!")
elif age >14 and age <=17:
    print("You get  a burger for breakfast!")
else:
    print("You are too old for breakfast!")
