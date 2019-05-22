### Mosquitto

Topic on the jetson side - face/image

Topic on the IBM VSI side - remoteface/image

QoS used was the default of 0

IBM object storage link - https://s3.us-south.cloud-object-storage.appdomain.cloud/w251-divya

Notes to myself: 
1. When starting the mosquitto broker container remember to map the ports
sudo docker run --name mosquitto --network hw03 -p 1883:1883 mosquitto

2. To capture the video inside the container map the device
sudo docker run --name detector --network hw03 --device=/dev/video1:/dev/video1 -ti detector /bin/bash
