HW 09 Answers

•	How long does it take to complete the training run? (hint: this session is on distributed training, so it will take a while) \
  It took approximately 2days and  11 hours to train around 120K steps

•	Do you think your model is fully trained? How can you tell? \
  I think it is trained since the train loss has reduced and has flattened out to a point where it might not reduce further.

•	Were you overfitting? \
  I don't think the model was overfitting since the train loss and eval loss are approximately at the same rate. Also I didn't train it   till too long. Also I think there is enough training data.

•	Were your GPUs fully utilized? \
  The GPUs were fully utilized

•	Did you monitor network traffic (hint: apt install nmon ) ? Was network the bottleneck? \
  The network was not the bottleneck, even though we were allocated  1000 Mbps looks like the internal network is faster than advertised, the rate was at 203551.3 KB/s for receive and 196851.3 KB/s for transmit
  
•	Take a look at the plot of the learning rate and then check the config file. Can you explain this setting? \
  The learning rate was based on the transformer policy. Increasing the learning rate linearly for the first warmup_steps training steps,
  and decreasing it thereafter proportionally to the inverse square root of the step number. We see that variation in the graph

•	How big was your training set (mb)? How many training lines did it contain? \
  train.clean.en.shuffled.BPE_common.32K.tok – 959MB – 4524869 lines \
  train.clean.de.shuffled.BPE_common.32K.tok – 1023MB – 4524869 lines

•	What are the files that a TF checkpoint is comprised of? \
  It consists of the checkpoint, the model data, index and meta files \
  checkpoint \
  events.out.tfevents.timestamp.hostname \
  graph.pbtxt \
  model.ckpt-0.data-00000-of-00001 \
  model.ckpt-0.index \
  model.ckpt-0.meta

•	How big is your resulting model checkpoint (mb)?  \
  The resulting model checkpoint was 853MB

•	Remember the definition of a "step". How long did an average step take? \
  The average step took around 1.6 seconds

•	How does that correlate with the observed network utilization between nodes? \
  In general if there is a bottleneck in the network then the time taken by a step may be more, but in our case we saw that    the network utilization between nodes was not a problem, we were provisioned more than the allocated network. 
