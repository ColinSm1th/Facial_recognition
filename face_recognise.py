import cv2
import pickle##

video = cv2.VideoCapture(0)
cascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

recognise = cv2.face.LBPHFaceRecognizer_create()##
recognise.read("trainner.yml")##

labels = {}##
with open("labels.pickle", "rb") as f:##
    og_label = pickle.load(f)##
    labels = {v:k for k,v in og_label.items()}##
    print(labels)

id_ = "0"
sampleno = 0

while True:
    check,frame = video.read()
    gray = cv2.ctvColor(frame, cv2.COLOR_BGRGRAY)

    face = cascade.detectMultiScale(gray, scaleFactor = 1.2, minNeighbors = 5)
    print(face)