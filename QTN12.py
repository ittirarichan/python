# factorial of n numbers

a=int(input("Enter a number to find factorial"))
f=1
for i in range(1,a+1):
    f=(f*i)
print("factorial is",f)
