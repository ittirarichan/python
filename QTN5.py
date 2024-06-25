# Write a program to check whether the last digit of a number( entered by user ) is 
# divisible by 3 or not.


a=float(input("Enter Numbers"))
d=a%10
if d%3==0:
    print("Divisible")
else:
    print("Not divisible")