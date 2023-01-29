import cv2
import os
import numpy as np
from PIL import Image
import pickle

cascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

recognise = cv2.face.LBPHFaceRecognizer_create()
def getdata():

    current_id = 0
    label_id = {} #dictionanary
    face_train = []
    face_label = []

    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    my_face_dir = os.path.join(BASE_DIR, 'image_data')

    for root, dirs, files in os.walk(my_face_dir):
        for file in files:
            if file.endswith("png") or file.endswith("jpg"):
                path = os.path.join(root, file)
                label = os.path.basename(root).lower()

                if not label in label_id:
                    label_id[label] = current_id
                    current_id +=1
                ID = label_id[label]

            #print(label_id)

                pil_image = Image.open(path).convert("L")
                image_array = np.array(pil_image, "uint8")
            #cv2.resize(image_array, (650,500))
                #print(type(image_array))