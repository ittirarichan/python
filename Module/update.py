def update(data):
    f=0
    a_name=input("Enter existing name ")
    for i in data:
        if a_name == i['name']:
            age=int(input("Enter new age" ))
            i['age']=age
            f=1
    if f==0:
        print("The name",a_name,"not in thelist ")