from reg import *
from dis import *
from update import *
data=[]
while True:
    print("1.Add \n2.Diaplay \n3.Update \n4.Delete \n5.Exit")
    ch=int(input("Enter ur choice "))
    if ch==1:
        register(data)
    elif ch==2:
        display(data)
    elif ch==3:
        update(data)
    elif ch==4:
        dele(data)
    elif ch==5:
        exit(data)