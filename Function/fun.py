# a=20
# def fun1():
#     a=13
#     a+=10
#     print('Welcome',a)
# fun1()
# print('Hello',a)





# a=20
# def fun1():
#     global b
#     print('Welcome',a)
# fun1()
# print('Hello',a)





# a=20
# def fun1():
#     global b
#     b=10
#     print('Welcome',b)
#     c=25
#     return c,74
# c1,c2=fun1()
# print('Hello',c1,c2)






# def add(a,b):
#     return a+b
# print(add(10,20))
# print(add(10,30))
# print(add('asd','a2123'))





# def add(name,age=24):
#     return name,age
# print(add("sanu",23))
# print(add("manu"))




# def add(name,age):
#     print("name:",name)
#     print("age:", age)
# add('anu',25)
# add(age=24,name="sanu")




# def add(*a):
#     return a
# print(add("anu",24))
# print(add())




# def add(**a):
#     return a
# print(add(name="anu",age=24))
# print(add())

# add=lambda a,b:a+b
# print(add(10,5))
# def add1(a,b):
#     return a+b



# add=lambda a,b:a+b
# def add1(a,b):
#     return a+b

# sub=lambda a,b:a-b
# def add1(a,b):
#     return a-b

# def mul(a,b):
#     return a*b
# def div(a,b):
#     return a/b
# def nbr():
#     a=int(input("Enter first number"))
#     b=int(input("Ener second no"))
#     return a,b

# while True:
#     print("\n1.add \n2.sub \n3.mul \n4.div \n5.exit \n")
#     ch=int(input("Enter your choice"))
#     if ch==1:
#         a,b=nbr()
#         print(add(a,b))
#     elif ch==2:
#         a,b=nbr()
#         print(sub(a,b))
#     elif ch==3:
#         a,b=nbr()
#         print(mul(a,b))
#     elif ch==4:
#         a,b=nbr()
#         print(div(a,b))
#     elif ch==5:
#         break


# l=[1,2,3,4,5,6]
# data=map(lambda a:a*2,l)
# print(data)
# print(list(data))


# def fun(a):
#     return a**2
# data1=map(fun,l)
# print(list(data1))


# l=[1,2,3,4,5,6]
# data=filter(lambda a:a%2==0,l)
# 
# def fun(a):
    # return a>=3
# data=filter(fun,l)
# print(list(data))



# l=["apple","Mango"]
# def fun1(a):
#     return a[0]=='a'
# data1=filter(fun1,l)
# print(list(data1))



import functools
l=[1,2,3,4,5]
data=functools.reduce(lambda total,value:total*value,l)
print(data)