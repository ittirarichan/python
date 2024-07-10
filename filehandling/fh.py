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


a = int(input("Enter a number: "))
filename = 'python/filehandling/multiplicationtable.txt'

with open(filename, 'w') as f:
    for i in range(1, a + 1):
        f.write(f"Multiplication Table for {i}:\n")
        for j in range(1, 11):
            f.write(f"{j} * {i} = {i * j}\n")
            f.write("\n")
