from cgi import print_arguments
from logging import root
import qrcode
from csv import writer
import os
import image
import cv2
from pyzbar.pyzbar import decode
import csv
import datetime

path1='codes/'
path2='images/'

def outImage(MIS):

    img = cv2.imread(os.path.join(path2,MIS+".jpg"))
    cv2.imshow('image', img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


def decodeQR():
    cap = cv2.VideoCapture(0)
    cap.set(cv2.CAP_PROP_FRAME_WIDTH,960)
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT,720) 

    MIS=0
    while True:
        check, frame= cap.read()
        cv2.imshow("Capturing", frame)
        for barcode in decode(frame):
            MIS=barcode.data.decode('utf-8')

        if MIS!=0 :
            break

        key=cv2.waitKey(1)
        if key==ord("q"):
            break

    name=""
    with open("register.csv","r") as file:
        reader=csv.reader(file)
        for row in reader:
            if row[0]==MIS:
                name=row[1]
                break

    now = datetime.datetime.now()
    date=now.strftime("%Y-%m-%d")
    time=now.strftime("%H:%M:%S")

    List=[MIS,name,date,time]

    with open('attendance.csv', 'a') as f_object:
        writer_object = writer(f_object)
        writer_object.writerow(List)
        f_object.close()

    cap.release()
    cv2.destroyAllWindows()
    outImage(MIS)