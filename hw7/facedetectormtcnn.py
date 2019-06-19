import numpy as np
import cv2
import paho.mqtt.client as mqtt
from mtcnn.mtcnn import MTCNN

# 1 should correspond to /dev/video1 , your USB camera. The 0 is reserved for the TX2 onboard camera
cap = cv2.VideoCapture(1)

# mosquitto broker address
broker_address="172.18.0.2"
#create new instance of client
client = mqtt.Client("facepub")
#connect to broker
client.connect(broker_address)

while(True):
    # frame rate
    print('frame rate', cv2.CAP_PROP_FPS)
    # Capture frame-by-frame
    ret, frame = cap.read()

    # face detection and other logic goes here
    detector = MTCNN()
    results = detector.detect_faces(frame)
    # extract the bounding box from the first face
    x1, y1, width, height = results[0]['box']
    x2, y2 = x1 + width, y1 + height
    img = frame[y1:y2, x1:x2]
    rc, png = cv2.imencode('.png', img)
    message = png.tobytes()
    # publish the face image
    client.publish("face/image", message)
