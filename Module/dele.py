def delete(data):
    b_name=input("Enter the existing name")
    for i in data:
         if b_name ==  i['name']:
            data.remove(i)
            print(b_name,"is deleted ")
         else:
             print(b_name,"is not deleted")