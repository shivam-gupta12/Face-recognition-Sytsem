import cv2
import numpy as np
import os
#recognizer = cv2.face.LBPHFaceRecognizer_create()
recognizer.read('trainer/trainer.yml')
cascadePath = "haarcascade_frontalface_default.xml"
faceCascade = cv2.CascadeClassifier(cascadePath);

cap = cv2.VideoCapture(0)
rec = cv2.createLBPHFaceRecognizer();
rec.load("F:/Program Files/projects/face_rec/faceREC/trainingdata.yml")
id = 0
font = cv2.cv.InitFont(cv2.cv.CV_FONT_HERSHEY_COMPLEX_SMALL, 5, 1, 0, 4)
while 1:
    ret, img = cap.read()
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.5, 5)
    for (x, y, w, h) in faces:
        cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)
        id, conf = rec.predict(gray[y:y + h, x:x + w])
        if (id == 2):
            id = "alok"
        if id == 1:
            id = "alok"
        if id == 3:
            id = "anjali"
        if id == 4:
            id = "Gaurav"
        if id == 5:
            id = 'rahul'
        if id == 6:
            id = "akshay"
        cv2.cv.PutText(cv2.cv.fromarray(img), str(id), (x, y + h), font, 255)
    cv2.imshow('img', img)

    if cv2.waitKey(1) == ord('q'):
        break
cap.release()

cv2.destroyAllWindows()

