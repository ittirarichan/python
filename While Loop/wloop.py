# i=0
# while i<=10:
    # print(i)
    # i+=1




# multiplication
# a=int(input("Enter a number"))
# i=1
# while i<=10:
#     print(i,"*",a,"=",a*i)
#     i+=1



# factorial
# a=int(input("Enter a number to find factorial"))
# i=1
# f=1
# while i<=a:
#     f=(f*i)
#     i+=1
# print("factorial is",f)




a=int(input("Enter starting number"))
b=int(input("Enter ending number"))
sum=0
esum=0
osum=0
i=a
while i<=b:
    sum+=i
    if i%2==0:
        esum=esum+i
    else:
        osum=osum+i
    i+=1
print("Sum of all numbers",sum)
print("sum of even numbers is",esum)
print("Sum of odd numbers is",osum)
