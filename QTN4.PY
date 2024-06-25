
# Accept any city from the user and display monument of that city.
#                   City                                 Monument
#                   Delhi                               Red Fort
#                   Agra                                Taj Mahal
#                   Jaipur                              Jal Mahal


a=input("Enter Any City in the given list(Delhi,agra,jaipur)")
if a=="Delhi":
    print("Monument of Delhi is Red Fort")
elif a=="Agra":
    print("Monument of Agra is Taj Mahal")
elif a=="Jaipur":
    print("Monument of Jaipur is Jal Mahal")
else:
    print("The given input is invalid")