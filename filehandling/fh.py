# f=open('python/filehandling/new4.txt','w')
# f.write('123'+'Abhi')


# f=open('python/filehandling/school.txt','w')
# f.write('123'+'Abhishek')


n=int(input("Enter the limit: "))
f=open('python/filehandling/sample.txt','w')
for i in range(n):
    a=input("Enter the name")
    f.write(a)