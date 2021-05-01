from tkinter import *

root=Tk()
root.geometry('400x500')
root.title('Subimission Form')

def getvalue():
    print(uservalue.get())
    print(passvalue.get())

username=Label(root,text='Username')
password=Label(root,text='Password')
username.grid()
password.grid()

uservalue = StringVar()
passvalue = StringVar()
foodservicevalue=IntVar()

userentry=Entry(root,textvariable=uservalue)
passentry=Entry(root,textvariable=passvalue)
userentry.grid(row=0,column=1)
passentry.grid(row=1,column=1)

foodservice=Checkbutton(root,text='want to pre-order your meal?',variable=foodservicevalue)
foodservice.grid(row=2,column=1)

Button(root,text='submit',command=getvalue).grid(row=3,column=1)

root.mainloop()