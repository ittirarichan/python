# class sample:
#     def display(self):
#         print("Sample class display method")

#     def s1(self):
#         print("Sample class s1 method")

# class demo(sample):
#     def display(self):
#         print("Start")
#         print("Demo class display method")
#         super().display()

#     def d1(self):
#         print("demo class d1 method")

# obj=demo()
# obj.display()





# To pass Value

# class sample:
#     def __init__(self,name,age):
#         print("Sample class display method")
#         print(name,age)

#     def s1(self):
#         print("Sample class s1 method")

# class demo(sample):
#     def __init__(self,name,age):
#         print(name,age)
#         print("Start")
#         print("Demo class display method")
#         super().__init__(name,age)

#     def d1(self):
#         print("demo class d1 method")

# obj=demo('akhil',25)

# class sample:
#     def display(self,name,age):
#         print("Sample class display method")
#         print(name,age)

#     def s1(self):
#         print("Sample class s1 method")

# class demo(sample):
#     def display(self,name,age):
#         print(name,age)
#         print("Start")
#         print("Demo class display method")
#         super().display(name,age)

#     def d1(self):
#         print("demo class d1 method")

# obj=demo()
# obj.display('akhil',25)