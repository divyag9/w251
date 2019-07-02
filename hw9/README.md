HW 09
•	How long does it take to complete the training run? (hint: this session is on distributed training, so it will take a while) – 124K steps – 2days 13 hours

•	Do you think your model is fully trained? How can you tell?

•	Were you overfitting? – not really since the train loss and eval loss are approximately same, the train loss is not very low

•	Were your GPUs fully utilized? – GPU fully utilized

•	Did you monitor network traffic (hint: apt install nmon ) ? Was network the bottleneck? No 

•	Take a look at the plot of the learning rate and then check the config file. Can you explain this setting? - varying the learning rate during the course of training

•	How big was your training set (mb)? How many training lines did it contain?
958585615 Jun 30 19:00 train.clean.en.shuffled.BPE_common.32K.tok – 914MB – 4524869 lines
1022911003 Jun 30 19:12 train.clean.de.shuffled.BPE_common.32K.tok – 976MB – 4524869 lines

•	What are the files that a TF checkpoint is comprised of? - 

•	How big is your resulting model checkpoint (mb)? - 852267044

•	Remember the definition of a "step". How long did an average step take? 1.6 seconds

•	How does that correlate with the observed network utilization between nodes?
