def update(data):
    f=0
    a_name=input("Enter existing name ")
    for i in data:
        if a_name in i:
            age=int(input("Enter new age" ))
            i[1]=age
            f=1
    if f==0:
        print("The name",a_name,"not in thelist ")