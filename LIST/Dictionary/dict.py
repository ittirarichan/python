std={'Name':'Akhil','Age':21,'Place':'EKM'}
# print(std['Name'])

# std['name']="Manu"
# print(std['name'])


# std['Mark']=50
# print(std['Mark'])

# for i in std:
    # print(i,std[i])

# print(std.pop('Age'))
# print(std.keys())

# print(std.items())

# std.setdefault("House Name")
# print(std)

# std.pop


# std1=std.fromkeys(1)

# std1=std
# print(id(std1))

# print(std.popitem())


a=int(input("How many"))
dtl=[]
for i in range(a):
    name=input("Name")
    age=int(input("Age"))
    nbr=int(input("Phone"))
    place=input("Place")
    dtl.append({"Name":name,"Age":age,"Phone":nbr,"Place":place})
    print("{:<10}{:16}".format("Name","Age","Phone","Place"))
    print("_"*20)
    for i in dtl:
        print("{:<10}{:16}".format(i["Name"],i["Age"],i["Phone"],i["Place"]))

