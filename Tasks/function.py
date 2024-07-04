
def add(a,b):
    return a+b
def sub(a,b):
    return a-b
def mul(a,b):
    return a*b
def div(a,b):
    return a/b
def nbr():
    a=int(input("Enter first number"))
    b=int(input("Ener second no"))
    return a,b

while True:
    print("\n1.add \n2.sub \n3.mul \n4.div \n5.exit \n")
    ch=int(input("Enter your choice"))
    if ch==1:
        a,b=nbr()
        print(add(a,b))
    elif ch==2:
        a,b=nbr()
        print(mul(a,b))
    elif ch==3:
        a,b=nbr()
        print(mul(a,b))
    elif ch==4:
        a,b=nbr()
        print(div(a,b))
    elif ch==5:
        break