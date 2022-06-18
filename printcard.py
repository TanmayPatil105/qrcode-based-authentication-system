import pandas as pd
from tkinter import *
from PIL import Image
from PIL import ImageTk
from PIL import ImageDraw
from PIL import ImageFont
import csv



font = ImageFont.truetype("fonts/B20Sans.ttf", 25, encoding="unic")

def generate_card(students):
    
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
                DOB=row[3]
                break

    template = Image.open("templates/template.png")
    pic = Image.open(f"codes/{MIS}.png").resize((165, 190), Image.ANTIALIAS)
    template.paste(pic, (25, 75, 190, 265))
    draw = ImageDraw.Draw(template)
    draw.text((315, 80), str(MIS),font=font ,fill='brown')
    draw.text((315, 125), name, font=font, fill='brown')
    draw.text((315, 170), contact,font=font, fill='brown')
    draw.text((315, 215), DOB,font=font,fill='brown')
    template.save(f"idcards/"+MIS+".png")

    im=Image.open("idcards/"+MIS+".png")
    im.show()

    win=Tk()
    win.title("Alert")
    win.geometry("600x200+50+50")
    Label(win, text= "ID card saved succesfully", font=('Mistral 18 bold')).place(x=150,y=80)
    win.bind('<Escape>', lambda e: win.destroy())

