# print even numbers sum in a range

a=int(input("Enter starting number"))
b=int(input("Enter ending number"))
sum=0
for i in range(a,b+1):
    if i%2==0:
        sum=sum+i
print(sum)