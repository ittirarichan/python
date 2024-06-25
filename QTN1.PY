# A company decided to give bonus of 5% to employee if his/her year of service is more 
# than 5 years.Ask user for their salary and year of service and print the net bonus amount.
    
a=float(input("Enter your salary"))
b=float(input("Enter total year of service"))
if(b>5):
        bns=(a*0.05)+a
        print("You are eligible Your net amount is",bns )
else:
    print("You are not eligible")
