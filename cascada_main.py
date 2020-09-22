import numpy as np
import cv2
import os
import matplotlib.pyplot as plt

folder = 'recursos cascada'
face = 'haarcascade_frontalface_default.xml'
facepath = os.path.join(folder,face)

def face_cascade(img,facepath):

    faceCascade =  cv2.CascadeClassifier(facepath)

    img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    faces = faceCascade.detectMultiScale(img_gray,1.1,4)

    for (x, y, w,h) in faces:
        cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)

    cv2.imshow('imagen',img)
    cv2.waitKey(1)
    plt.show()
    
cap = cv2.VideoCapture(1)

while True:
    
    sucess,img = cap.read()
    
    face_cascade(img,facepath)
    
    if(cv2.waitKey(1) & 0xFF == ord('q')):
        break