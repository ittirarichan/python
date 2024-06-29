# a=input("Enter what do you need  ")
# l=["Abhi","Alan","Akhil","Amal","Alan",10,20,30,40,50,60]
# if a in l:
    # print(a,"in list")
# else:
    # print(a,"not in the list")




# l=["Abhi","Anandhu","Nikhil",20,30]
# l.append("Aju")
# l.append([10,40])
# l.insert(2,35)
# l.extend(["irffan","Amal,Alen"])
# print(l)





# l=[1,2,3,4,5,6,7,["a","b","c"],45,66,77,88,99]
# l.remove(3)
# l.pop()
# l.pop(5)
# # l.clear()
# print(l)





# l=[21,25.35]
# print(l.index(1))
# print(l.count(2))
# print(l.reverse)
# l.sort()
# l.reverse()
# print(l)





# a=int(input("Enter how many students"))
# name=[]
# for i in range(a):
#     n=input("Enter Students Name")
#     name.append(n)
# print(name)





# add a new list from existing list by without reduntent
# l=[1,2,3,4,1,2,3,4]
# a=[]
# for i in l:
    # if i not in a: 
        # a.append(i)
# print(a)





# l=['manu','akhil','sonu']
# for i in l:
    # rev=''
    # for j in i:
        # rev=j+rev
    # print(rev)





# sum of the list without characters
# l=[1,2,3,'abc',20.5]
# n=0
# for i in l:
    # if type(i)==int:
        # n+=i
    # elif type(i)==float:
        # n+=i
# print(n)






# largest number
l=[1,2,10,65,20,3]
n=l[0]
for i in l:
    if i>n:
        n=i
print("The largest number in the list is:",n)
        