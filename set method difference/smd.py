# x={"apple","banana","Mango"}
# y={"kiwi","apple,cheera"}
# z=x.difference()
# print(z)

# x = {"apple", "banana", "Mango"}
# y = {"kiwi", "apple", "cheera"} 
# z = x.union(y) 
# print(z)


# x = {"apple", "banana", "Mango"}
# y = {"kiwi", "apple", "cheera"} 
# z = x.intersection(y) 
# print(z)


x={"apple","banana","Mango"}
y={"kiwi","apple,cheera"}
z=y.difference_update(x)
print(z)
