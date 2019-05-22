import numpy as np
import cv2
import paho.mqtt.client as mqtt

# 1 should correspond to /dev/video1 , your USB camera. The 0 is reserved for the TX2 onboard camera
cap = cv2.VideoCapture(1)

# mosquitto broker address
broker_address="172.18.0.2"
#create new instance of client
client = mqtt.Client("facepub")
#connect to broker
client.connect(broker_address)

while(True):
    # Capture frame-by-frame
    ret, frame = cap.read()

    # We don't use the color information, so might as well save space
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    # face detection and other logic goes here
    face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)
    for (x,y,w,h) in faces:
    	# your logic goes here
	roi_gray = gray[y:y+h, x:x+w]
	rc, png = cv2.imencode('.png', roi_gray)
	message = png.tobytes()
	# publish the face image
	client.publish("face/image", message)
