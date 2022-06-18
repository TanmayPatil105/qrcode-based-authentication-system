from cgi import print_arguments
from logging import root
import qrcode
from csv import writer
from tkinter import *
from PIL import Image ,ImageTk
import os
import image
import cv2
from pyzbar.pyzbar import decode
import csv
import datetime
import generate
import scan
import details
import printcard


## TO APPEND ALL MIS IN students ARRAY

students=[]
with open("register.csv","r") as file:
    reader=csv.reader(file)
    for row in reader:
        students.append((row[0]))


## COLORS FOR TERMINAL

class bcolors:
    HEADER = '\033[95m'
    OKWHITE = '\033[37m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

while (True):
    os.system('clear')
    print("\033[0;33m")
    print("\n\t\t\t\t\t***************************************************************************\n")
    print("\n\t\t\t\t\t\t\t\t   WELCOME TO COEP \n\n")
    print("\t\t\t\t\t****************************************************************************\n")
    print("\033[0m")
    print("\n\t\t\t\t\t\t\t\t"+bcolors.WARNING+"Enter 1 to Register\n\t\t\t\t\t\t\t\tEnter 2 to Scan QR code\n\t\t\t\t\t\t\t\tEnter 3 to get Details\n\t\t\t\t\t\t\t\tEnter 4 to print ID CARD\n\t\t\t\t\t\t\t\tEnter 5 to EXIT")
    i=int(input("\n\t\t\t\t\t\t\t\tEnter --->"))
    if(i==1):
        os.system('clear')
        generate.register(students)
    elif(i==2):
        os.system('clear')
        if(scan.decodeQR(students)==0):
            win=Tk()
            win.title("Alert")
            win.geometry("600x200+50+50")
            Label(win, text= "Process Aborted", font=('Mistral 18 bold')).place(x=150,y=80)
            win.bind('<Escape>', lambda e: win.destroy())
        
    elif(i==3):
        os.system('clear')
        details.getDetails(students)
    elif (i==4):
        os.system('clear')
        printcard.generate_card(students)
        
    else :
        break
