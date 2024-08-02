# import tkinter 
# from tkinter import messagebox
# app=tkinter.Tk()

# def data():
#     v=v1.get()
#     l2.config(text=v)
#     # messagebox.askretrycancel("warning",v1.get)
#     # messagebox.askquestion("warning",v1.get())
#     if v_c1.get()==1:
#         print("Mal selected")
#     if v_c2.get()==1:
#         print("Eng selected")
    
#     print(vr1.get())


# app.title("SYNNEFO")
# app.minsize(400,400)
# app.maxsize(600,600)
# app.config(bg="gray")
# l1=tkinter.Label(app,text="WELCOME",bg="black",fg="white")
# l1.pack()
# v1=tkinter.StringVar()
# e1=tkinter.Entry(app,textvariable=v1)
# e1.pack()

# v_c1=tkinter.IntVar()
# v_c2=tkinter.IntVar()
# c1=tkinter.Checkbutton(app,text="mal",variable=v_c1)
# c1.pack()
# c2=tkinter.Checkbutton(app,tex="eng",variable=v_c2)
# c2.pack()

# vr1=tkinter.IntVar()
# r1=tkinter.Radiobutton(app,text="male",value=1,variable=vr1)
# r2=tkinter.Radiobutton(app,text="female",value=2,variable=vr1)
# r1.pack()
# r2.pack()

# b1=tkinter.Button(app,text="OK",bg="white",fg="black",activebackground="red",activeforeground="white",padx=5,pady=5,command=data)
# b1.pack()

# l2=tkinter.Label(app,background='gray')
# l2.pack()

# app.mainloop()




import tkinter
app=tkinter.Tk()
c=tkinter.Canvas(app,width=400,height=400,bg='red')
# c.create_line(150,250,250,150)
c.create_rectangle(50,50,350,250,fill="white")
c.create_oval(50,50,360,250,fill='gray')
c.create_oval(25,25,0,250,fill='gray')
c.pack()
app.mainloop()