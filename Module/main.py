from reg import *
from display import *
from update import *
from dele import *
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
        delete(data)
    elif ch==5:
        exit(data)