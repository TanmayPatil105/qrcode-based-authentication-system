from tkinter import *
from PIL import Image ,ImageTk
import csv

def getDetails(students):

    MIS=input("\n\t\t\t\t\t\t\t\tEnter Your MIS : \033[92m")
    if MIS not in students:
        win=Tk()
        win.geometry("600x200+50+50")
        win.title("Alert")
        Label(win, text= "Student not Registered", font=('Mistral 18 bold')).place(x=150,y=80)
        win.bind('<Escape>', lambda e: win.destroy())
        return
    
    with open("register.csv","r") as file:
        reader=csv.reader(file)
        for row in reader:
            if row[0]==MIS:
                name=row[1]
                contact=row[2]
                break
    
    label=Tk()
    label.title("Details")
    label.geometry("600x400+50+50")  

    label1=Label(label, text="Name : "+name, font=("Helvetica",20,"bold"))
    label1.pack( pady=10)

    label1=Label(label, text="MIS : "+ MIS, font=("Helvetica",20,"bold"))
    label1.pack(pady=10)

    label1=Label(label, text="Contact : "+ contact, font=("Helvetica",20,"bold"))
    label1.pack(pady=10)

    image = Image.open(f"images/{MIS}.jpg").resize((300,240), Image.ANTIALIAS)
    photo = ImageTk.PhotoImage(image)
    name = Label(image=photo)
    name.pack()

    label.bind('<Escape>', lambda e: label.destroy())
    label.mainloop()
