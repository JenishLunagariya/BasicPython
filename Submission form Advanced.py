'''Submission form with auto record in txt file'''
from tkinter import *

root=Tk()


root.geometry('400x300')
def getvalue():
    print(f"{namevalue.get(),phonevalue.get(),gendervalue.get(),foodservicevalue.get()}")

    with open('record.txt', 'a') as f:
        f.write(f"{namevalue.get(),phonevalue.get(),gendervalue.get(),foodservicevalue.get()}\n")


Label(root,text='welcome to root travels',font='arial 10 bold',).grid(column=2)
name=Label(root,text='name')
phone=Label(root,text='phone')
gender=Label(root,text='gender')
name.grid(row=2)
phone.grid(row=3)
gender.grid(row=4)

namevalue=StringVar()
phonevalue=IntVar()
gendervalue=StringVar()
foodservicevalue=IntVar()

nameentry=Entry(root,textvariable=namevalue)
phoneentry=Entry(root,textvariable=phonevalue)
genderentry=Entry(root,textvariable=gendervalue)

nameentry.grid(row=2,column=2)
phoneentry.grid(row=3,column=2)
genderentry.grid(row=4,column=2)

foodservice=Checkbutton(text='wan a prebook your meal?',variable=foodservicevalue)
foodservice.grid(row=5,column=2)

Button(root,text='submit',command=getvalue).grid(row=6,column=2)


root.mainloop()