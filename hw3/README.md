### MQTT

Topic on the jetson side - face/image
I should have named it jetson/image
The publisher publishes the face image read from the camera to the face/image topic.
The subscriber subcribes to face/image topic to receive the face image read from the camera and then forwards it to the remote by publishing to the remoteface/image topic.
I could have more topics like face/video and have a subscriber subcribing to all images and videos like face/#

Topic on the IBM VSI side - remoteface/image
I should have named it remote/image
The subscriber subcribes to remoteface/image to receive the face image from the jetson and uploads to object storage.
I could have more topics like remoteface/video and have a subscriber subcribing to all images and videos like remoteface/#

QoS used was the default of 0- In the case of this homework we didn't need a guarantee of every message being delivered, also we had a stable connection between the sender and receiver.

IBM object storage link - https://s3.us-south.cloud-object-storage.appdomain.cloud/w251-divya

#### Steps performed:
##### Jetson
1. create network bridge
   sudo docker network create --driver bridge hw03
2. create mosquitto container
   sudo docker run --name mosquitto --network hw03 -p 1883:1883 mosquitto
3. create face detetctor container
   sudo docker run --name detector --netwrok hw03 --device=/dev/video1:/dev/video1 detector /bin/bash
   once inside bash run - python facedetector.py
4. create forwarder container to forward the messages(faces) to VSI
   sudo docker run --name forwarder --netwrok hw03 -ti faceforwarder sh
   once inside shell client run - python faceforwarder.py

##### IBM VSI
1. create network bridge
   docker network create --driver bridge hw03
2. create mosquitto container
   docker run --name mosquitto --network hw03 -p 1883:1883 mosquitto
3. create upload container to upload the faces to object storage
   docker run --name subscriber --network hw03 -ti subscriber sh
   once inside shell client run - python upload.py

Notes to myself: 
1. When starting the mosquitto broker container remember to map the ports
sudo docker run --name mosquitto --network hw03 -p 1883:1883 mosquitto

2. To capture the video inside the container map the device
sudo docker run --name detector --network hw03 --device=/dev/video1:/dev/video1 -ti detector /bin/bash
