# print("welcome")
# print('hello')

# name="Abhishek"
# age="21"
# weight="65"
# print("Name:",name)
# print("Age:",age)
# print("Weight:",weight)


# a=20+1j
# print(type(a))

# a=20
# print(type(a))

# a=20.6
# print(type(a))

# a="Abhi"
# print(type(a))

# a=True
# print(type(a))

# a=(20,30,40,)
# print(type(a))

# a=[20,30,40]
# print(type(a))

# a={20,20,39}
# print(type(a))

# a={"name":"Abhi","age":21}
# print(type(a))




# 22/06/24

# name=input("Enter name")
# age=int(input("Enter age"))
# weight=float(input("Enter weight"))
# print("Name",name,"\n","Age",age,"\n","Weight",weight)

# a=10
# b=5
# print(a+b)

# a=10
# b=5
# print(a-b)

# a=10
# b=5
# print(a*b)
# 
# a=10
# b=5
# print(a/b)

# a=10
# b=5
# print(a%b)

# a='Abhi'
# b=5
# print(a*b)


# a=10
# b=5
# print(a//b)


# a=int(input("Enter a integer number"))
# b=int(input("Enter another integer number"))
# c=a+b
# print(c)


# a=10
# a+=10
# print(a)


# a=10
# a-=20
# print(a)

# a=10
# a*=10
# print(a)

# a=20
# a%=5
# print(a)

# a=20
# a/=5
# print(a)


# a=10
# a//=5
# print(a)


# a=10
# a**=3
# print(a)

# a=10
# b=10
# print(a==b)

# a=10
# b=2
# print(a==b)

# a=10
# b=9
# print(a!=b)

# a=10
# b=10
# print(a!=b)


# a=10
# b=11
# print(a<b)

# a=12
# b=11
# print(a<b)


# a=12
# b=11
# print(a>b)

# a=12
# b=13
# print(a>b)

# a=10
# b=10
# print(a<=b)

# a=12
# b=11
# print(a<=b)

# a=12
# b=11
# print(a>=b)

# a=12
# b=14
# print(a>=b)

# a=10
# b=10
# print(not(a==a or a>=b))

# a=10
# # b=15
# print(a==b and a<=b)


# a=10
# b=15
# print(a!=b or a>b)

# a="Abhishek"
# print('A' in a)

# a="Abhishek"
# print('J' in a)

# a="Abhishek"
# print('A' not in a)

# a="Abhishek"
# print('z' in a)

# a=10
# b=10
# print(id(a))
# print(id(b))
# print(a is b)

# l=[1,2,3,4]
# l1=[1,2,3,4]
# print(id(l))
# print(id(l1))
# print(l is l1)


# a=float(input("Enter a number"))
# b=float(input("Enter another number"))

# if a>b:
#     print(a)
# else:
#     print(b)

# a=float(input("Enter a number"))
# b=float(input("Enter another number"))

# if a!=b:
#     print(True)
# else:
#     print("False")



# A company decided to give bonus of 5% to employee if his/her year of service is more 
# than 5 years.Ask user for their salary and year of service and print the net bonus amount.
    
# a=float(input("Enter your salary"))
# b=float(input("Enter total year of service"))
# if(b>5):
#         bns=(a*0.05)+a
#         print("You are eligible Your net amount is",bns )
# else:
#     print("You are not eligible")






# Write a program to calculate the electricity bill (accept number of unit from user) 
# according to the following criteria :
#              Unit                                                     Price  
# First 100 units                                               no charge
# Next 100 units                                              Rs 5 per unit
# After 200 units                                             Rs 10 per unit
# (For example if input unit is 350 than total bill amount is Rs2000)

# a=float(input("Enter the number of units"))
# if a<=100:
    # print("No charge")
# elif a<=200:
    # b=(a-100)*5
    # print("Total bill amount is: ",b)
# else:
    # c=(a-200)*10+500
    # print("Total bill amount is: ",c)






# Write a program to accept a number from 1 to 7 and display the name of the day like 1 
# for Sunday , 2 for Monday and so on.

# a=int(input("Enter a number between 1 to 7"))
# if a==1:
#     print("Sunday")
# elif a==2:
#     print("Monday")
# elif a==3:
#     print("Tuesday")
# elif a==4:
#     print("Wednesday")
# elif a==5:
#     print("Thursday")
# elif a==6:
#     print("Friday")
# elif a==7:
#     print("saturady")
# else:
#     print("Invalid number")
