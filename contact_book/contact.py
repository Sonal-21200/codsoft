from tkinter import*
def save_data():
    nametext=name.get()
    phonetext=phone.get()
    with open('main.txt','a')as file:
        file.write(f"Name:  {nametext}\n")
        file.write(f"Phone:  {phonetext}\n")
root=Tk()
root.geometry('400x400')
Label(root,text="Name:").grid(row=0,column=0,padx=10,pady=10)
Label(root,text="Phone:").grid(row=1,column=0,padx=10,pady=10)

name=StringVar()
phone=StringVar()
Entry(root,textvariable=name).grid(row=0,column=1,pady=10)
Entry(root,textvariable=phone).grid(row=1,column=1,pady=10)

Button(root,text="Submit",command=save_data).grid(row=3,column=1)
root.mainloop()