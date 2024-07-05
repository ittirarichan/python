def register(data):
    id=int(input("\n Enter your id ID"))
    name=input("Enter your Name")
    age=int(input("Enter your Age"))
    place=input("Enter your Place")
    data.append({"ID":id,"Name":name,"Age":age,"Place":place})