# names=["manu","Akhil","Abhi",20,30]

# print(names)


# print ("manu" in names)
       

# print (names[3])


# if "manu"in names:
    # print("Yes")
# else:
    # print("No")


# for i in names:
    # print(i)




# a="welcome"
# b=""
# for i in a:
#     b=i+b
# print(b)





# * * *
# * * *
# * * *
# * * *
# for i in range(4):
#     for j in range(3):
#         print('*\n',end="")
#     print()





# 0 1 2
# 0 1 2
# 0 1 2
# for i in range(3):
#     for j in range(3):
#         print(j,end="\t")
#     print()





# 0 0 0
# 1 1 1
# 2 2 2
# for i in range(3):
    # for j in range(3):
        # print(i,end="\t")
    # print()





# 0 1 2
# 3 4 5
# 6 7 8
# a=0
# for i in range(3):
#     for j in range(3):
#         print(a,end="\t")
#         a+=1
#     print()





# 0 
# 1 1
# 2 2 2
# for i in range(3):
#     for j in range(i+1):
#         print(i,end="\t")
#     print()





# 0
# 0 1
# 0 1 2
# for i in range(3):
#     for j in range(i+1):
#         print(j,end="\t")
#     print()




# 0 
# 1 2
# 3 4 5
# a=0
# for i in range(3):
    # for j in range(i+1):
        # print(a,end="\t")
        # a+=1
    # print()




# 0
# 1 0
# 2 1 0
# for i in range(3):
#     for j in range(i+1):
#         print(i-j,end="\t")
#     print()





# A A A 
# B B B
# C C C
# a=65
# for i in range(3):
#     for j in range(3):
#         print(chr(a),end='\t')
#     print()
#     a+=1


# A B C 
# D E F 
# G H I
# a=65
# for i in range(3):
#     for j in range(3):
#         print(chr(a),end='\t')
#         a+=1
#     print()




# A B C 
# A B C 
# A B C 
# a=65
# for i in range(3):
#     for j in range(3):
#         print(chr(a),end="\t")
#     print()
#     a+=1





# A 
# A B 
# A B C 

# a=65
# for i in range(3):
#     for j in range(i+1):
#         print(chr(a+j),end="\t")
#     print()



# A 
# B B 
# C C C 
# a=65
# for i in range(3):
#     for j in range(3):
#         print(chr(a),end="\t")
#     print()
#     a+=1


# A
# B C 
# D E F 
# a=65
# for i in range(3):
#     for j in range(i+1):
#         print(chr(a),end="\t")
#         a+=1
#     print()





# A
# B A
# C B A
# a=65
# for i in range(3):
#     for j in range(i+1):
#         print(chr(a-j),end='\t')
#     print()
#     a+=1




# 1
# 0 1
# 1 0 1
# 0 1 0 1
# 1 0 1 0 1


# for i in range(1,6):
#     for j in range(i):
#         print((i+j)%2,end=" ")
#     print()




# #
# + +
# # # #
# + + + +
# # # # # #

# for i in range(1,6):
#     for j in range(i):
#         if i%2==0:
#             print('+',end=" ")
#         else:
#             print('#',end=" ")
#     print()