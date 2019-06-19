HW07

IBM object storage link - https://s3.us-south.cloud-object-storage.appdomain.cloud/w251-divya

* Describe your solution in detail. What neural network did you use? What dataset was it trained on? What accuracy does it achieve? \
For the face detection used multitask cascaded convolutional networks model instead of the OpenCV cascade face classifier. \
Neural Network:\
This model consists of  three-stage multi-task deep convolutional networks \
Dataset:\
WIDER FACE dataset was used for training. It consists of 393,703 labeled face bounding boxes \
in 32,203 images where 50% of them were used for testing into three
subsets according to the difficulty of images, 40% for training
and the remaining for validation \
Accuracy is around 95% \
https://arxiv.org/ftp/arxiv/papers/1604/1604.02878.pdf \
https://github.com/ipazc/mtcnn

* Does it achieve reasonable accuracy in your empirical tests? Would you use this solution to develop a robust, production-grade system? \
Yes 

* What framerate does this method achieve on the Jetson? Where is the bottleneck? \
It has a frame rate of 5, I think the detection of face through this model is little slower compared to opencv face detector 

* Which is a better quality detector: the OpenCV or yours? \
Both had equally good quality of detection
