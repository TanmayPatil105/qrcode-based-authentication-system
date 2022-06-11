from cgi import print_arguments
from logging import root
import qrcode
from csv import writer
from tkinter import *
import os
from PIL import Image ,ImageTk
import image
import cv2
import csv
import datetime

path1='codes/'
path2='images/'

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


def takepicture(MIS,name):
    key = cv2. waitKey(1)
    webcam = cv2.VideoCapture(0)

    while True:
        try:
            check, frame = webcam.read()
            cv2.imshow("Capturing", frame)
            key = cv2.waitKey(1)

            if key == ord('s'): 
                # cv2.putText(frame,name, 
                #     bottomLeftCornerOfText, 
                #     font, 
                #     fontScale,
                #     fontColor,
                #     thickness,
                #     lineType)
                frame = cv2.copyMakeBorder(frame, 5, 5, 5, 5, cv2.BORDER_CONSTANT, None, value = [88,88,88])
                cv2.imwrite(os.path.join(path2,MIS+".jpg"), img=frame)
                webcam.release()
                cv2.waitKey(1650)
                cv2.destroyAllWindows()
                return 1

            elif key == ord('q'):
                print("Turning off camera.")
                webcam.release()
                print("Camera off.")
                print("Program ended.")
                cv2.destroyAllWindows()
                return 0
        
        except(KeyboardInterrupt):
            print("Turning off camera.")
            webcam.release()
            print("Camera off.")
            print("Program ended.")
            cv2.destroyAllWindows()
            break
        


def register(students):
    qr = qrcode.QRCode(
        version =9,
        box_size =7,
        border=7)

    print(bcolors.OKBLUE)
    MIS=input("\t\t\t\t\t\t\t\tEnter Your MIS : \033[92m")
    print(bcolors.OKWHITE)

    if(MIS in students):
        win=Tk()
        win.geometry("600x200+50+50")
        win.title("Alert")
        Label(win, text= "MIS already Registered", font=('Mistral 18 bold')).place(x=150,y=80)
        return

    print(bcolors.OKBLUE)
    name=input("\t\t\t\t\t\t\t\tEnter Your name : \033[92m")
    print(bcolors.OKWHITE)

    print(bcolors.OKBLUE)
    contact=int(input("\t\t\t\t\t\t\t\tEnter Your Contact No. : \033[92m"))
    print(bcolors.OKBLUE)

    while len(str(contact))!=10 :
        contact=int(input("\t\t\t\t\t\t\t\tRe-Enter Your Contact No. : \033[92m"))
    print(bcolors.OKWHITE)

    print(bcolors.OKBLUE)
    DOB=input("\t\t\t\t\t\t\t\tEnter Your Date of Birth : \033[92m")
    print(bcolors.OKBLUE)

    print(bcolors.OKBLUE)
    Address=input("\t\t\t\t\t\t\t\tEnter Your Address : \033[92m")
    print(bcolors.OKBLUE)

    i=takepicture(MIS,name)
    if(i==0):
        win=Tk()
        win.geometry("600x200+50+50")
        Label(win, text= "Process Aborted", font=('Mistral 18 bold')).place(x=150,y=80)
        return

    qr.add_data(MIS)
    image = qr.make_image(fill_color="black", back_color= "white")
    image.save(f"{path1}/"+MIS+".png")

    List=[MIS,name,contact,DOB,Address]
    with open('register.csv', 'a') as f_object:
        writer_object = writer(f_object)
        writer_object.writerow(List)
        f_object.close()
    
    students.append(MIS)

    win=Tk()
    win.geometry("600x200+50+50")
    Label(win, text= "MIS Registered Successfully", font=('Mistral 18 bold')).place(x=150,y=80)
