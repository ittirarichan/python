def register(data):
    id=int(input("\nEnter your id ID "))
    name=input("Enter your Name" )
    age=int(input("Enter your Age "))
    place=input("Enter your Place ")
    data.append({"ID":id,"name":name,"age":age,"Place":place})