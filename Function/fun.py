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




def add(**a):
    return a
print(add(name="anu",age=24))
print(add())