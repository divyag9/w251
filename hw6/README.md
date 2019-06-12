HW6

### Runtimes

V100 is 3 times faster than P100


V100 1 epoch \
100% 1/1 [1:51:59<00:00, 6719.81s/it, avg_accuracy=0.952, avg_loss=0.121]
Validation run time
100% 15625/15625 [15:51<00:00, 16.30it/s]

V100 2 epochs
100% 2/2 [3:54:05<00:00, 7020.20s/it, avg_accuracy=0.961, avg_loss=0.0924]
Validation run time
100% 15625/15625 [15:50<00:00, 16.43it/s]

P100 1 epoch
100% 1/1 [6:04:32<00:00, 21872.93s/it, avg_accuracy=0.952, avg_loss=0.121]
Validation run time
100% 15625/15625 [1:00:41<00:00, 4.29it/s]

In case of V100 trained the model for 2 epochs

In case of P100 for training with 2 epochs, used the model that was originally trained for 1 epoch. Loaded the saved model trained the saved model for 1 more epoch with half the learning rate.
