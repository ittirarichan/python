# f=open('python/filehandling/new4.txt','w')
# f.write('123'+'Abhi')


# f=open('python/filehandling/school.txt','w')
# f.write('123'+'Abhishek')


# n=int(input("Enter the limit: "))
# f=open('python/filehandling/sample.txt','w')
# for i in range(n):
#     a=input("Enter the name")
#     f.write(a)


# a=int(input("Enter a number"))
# f=open('python/filehandling/multiplicationtable.txt','w')
# for i in range(1,11):
#     f.write(f"{i} * {a} = {a*i}\n")


# a = int(input("Enter a number: "))
# filename = 'python/filehandling/multiplicationtable.txt'

# with open(filename, 'w') as f:
#     for i in range(1, a + 1):
#         f.write(f"Multiplication Table for {i}:\n")
#         for j in range(1, 11):
#             f.write(f"{j} * {i} = {i * j}\n")
#             f.write("\n")


# f=open('python/filehandling/multiplicationtable.txt',"a")
# f.write("Python")


# f=open('python/filehandling/multiplicationtable.txt',"r")
# print(f.read())


# f=open("python/filehandling/multiplicationtable.txt","r")
# print(f.read(8))
# print("-","20")
# print(f.readline(2))
# print(f.read())
# print(f.read(2))


# f=open("python/filehandling/multiplicationtable.txt","r")
# print(f.readlines())
# print('-'*20)


# f=open("python/filehandling/multiplicationtable.txt","r")
# l=len(f.readlines())
# f.seek(0)-
# for i in range(1):
#     a=f.readline().strip()
#     print(a[::-1])


# f=open("python/filehandling/new4.txt","r")
# l=len(f.readlines())
# f.seek(0)
# word=(0)
# for i in range(1):
#     a=f.readline().strip()
#     for j in a:
#         if j == ' ':
#             word+=1
#     print(a[:-1])
#     word+=1



# f=open("python/filehandling/new4.txt","r")
# l=len(f.readlines())
# f.seek(0)
# word=(0)
# letter=(0)
# for i in range(1):
#     a=f.readline().strip()
#     for j in a:
#         if j == ' ':
#             word+=1
#         else:
#             letter+=1
#     print(a[:-1])
#     word+=1
# print(word)
# print(letter)





f=open("python/filehandling/new4.txt","r")
l=len(f.readlines())
f.seek(0)
word=0
letter=0
cap=0
for i in range(1):
    a=f.readline().strip()
    for j in a:
        if j == ' ':
            word+=1
        else:
            letter+=1
            if j.isupper():
                cap+=1
    print(a[:-1])
    word+=1
print(word)
print(letter)
print(cap)