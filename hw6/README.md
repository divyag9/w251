HW6

### Runtimes

Overall V100 is 3 times faster than P100


V100 1 epoch \
100% 1/1 [1:51:59<00:00, 6719.81s/it, avg_accuracy=0.952, avg_loss=0.121] \
Validation run time \
100% 15625/15625 [15:51<00:00, 16.30it/s]

V100 2 epochs \
100% 2/2 [3:54:05<00:00, 7020.20s/it, avg_accuracy=0.961, avg_loss=0.0924] \
Validation run time \
100% 15625/15625 [15:50<00:00, 16.43it/s]

P100 1 epoch \
100% 1/1 [6:04:32<00:00, 21872.93s/it, avg_accuracy=0.952, avg_loss=0.121] \
Validation run time \
100% 15625/15625 [1:00:41<00:00, 4.29it/s]

In case of V100 trained the model for 2 epochs

In case of P100 for training with 2 epochs, used the model that was originally trained for 1 epoch. Loaded the saved model trained the saved model for 1 more epoch with half the learning rate.

### AUC
V100 1 epoch - 0.96990
V100 2 epochs - 0.96968
P100 1 epoch - 0.96990
P100 2 epochs - 

### Sentences

1 epoch \
lowest toxicity - "Trump is a mentally unbalanced buffoon.\nHe's unfit for office.\nHe's the largest threat to our nation's security and Congress should exercise it's responsibility and remove him now.\nHe's a petty con man, a racist supremacist, a sexual predator and a traitor.\nWorst ever."

highest toxicity - "Rolling Stone supports the nationalization of the means of production*, democratization of the workplace*, income distribution*, food and education for the poor* and peace and prosperity*??  Who knew?\n\nWow, I should subscribe.\n\n\n*Look those things up"

2 epochs \
lowest toxicity - \
highest toxicity - \




