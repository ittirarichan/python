# std={'Name':'Akhil','Age':21,'Place':'EKM'}
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


# a=int(input("How many"))
# dtl=[]
# for i in range(a):
#     name=input("Name :")
#     Age=int(input("Age :"))
#     nbr=int(input("Phone :"))
#     place=input("Place :")
#     dtl.append({"Name":name,"Age":Age,"Phone":nbr,"Place":place})
# print("{:<10}{:16}{:<10}{:16}".format("Name","Age","Phone","Place"))
# print("_"*20)
# for i in dtl:
#     print("{:<10}{:16}{:<10}{:16}".format(i["Name"],i["Age"],i["Phone"],i["Place"]))

# print('Age>30')
# print("{:<10}{:16}{:<10}{:16}".format("Name","Age","Phone","Place"))
# for i in dtl:
#     if i['Age']>=30:
#         print("{:<10}{:16}{:<10}{:16}".format(i["Name"],i["Age"],i["Phone"],i["Place"]))

# print('Age<30')
# print("{:<10}{:16}{:<10}{:16}".format("Name","Age","Phone","Place"))
# for i in dtl:
#     if i['Age']<30:
#         print("{:<10}{:16}{:<10}{:16}".format(i["Name"],i["Age"],i["Phone"],i["Place"]))


# nbr={0:'Zero',1:'one',2:'Two',3:'Three',4:'Four',5:'Five',6:'Six',7:'Seven',8:'Eight',9:'nine'}
# num=[]
# a=int(input("Enter number"))
# result=''
# while a>0:
    # digit=a%10
    # word=nbr[digit]
    # result=word+''+result
    # a=a//10
# print(result)
# 