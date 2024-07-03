# Write a program to accept the cost price of a bike and display the road tax to be paid according to the 
# following criteria :
    
#         Cost price (in Rs)                                       Tax
#         > 100000                                                  15%
#         > 50000 and <= 100000                                     10%
#         <= 50000                                                  5%

a=float(input("Enter the Cost "))
if a>100000:
    a=(a*0.15)
    print("The road tax amount is",a)
elif a>500000 and a<=100000:
    a=(a*0.10)
    print ("The road tax amount is",a)
elif a<=500000:
    a=(a*0.05)
    print("The road tax amount is",a)
