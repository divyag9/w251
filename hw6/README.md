### HW6

### Runtimes

Overall V100 is 3 times faster than P100.\
In case of V100 for training with 2 epochs trained the model from the begining with 2 epochs.\
In case of P100 for training with 2 epochs, used the model that was originally trained for 1 epoch. Loaded the saved model and trained the saved model for 1 more epoch with half the learning rate( since the model was already trained, to avoid destroying the weights)


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

P100 after 2nd epoch \
100% 1/1 [6:10:04<00:00, 22204.65s/it, avg_accuracy=0.959, avg_loss=0.0975] \
Validation run time \
100% 15625/15625 [1:00:46<00:00, 4.29it/s]



### AUC
V100 1 epoch - 0.96990 \
V100 2 epochs - 0.96968 \
P100 1 epoch - 0.96990 \
P100 2 epochs - 0.96977

### Sentences

1 epoch \
P100 and V100 \
**highest toxicity** - "Trump is a mentally unbalanced buffoon.\nHe's unfit for office.\nHe's the largest threat to our nation's security and Congress should exercise it's responsibility and remove him now.\nHe's a petty con man, a racist supremacist, a sexual predator and a traitor.\nWorst ever." \
**lowest toxicity** - "Rolling Stone supports the nationalization of the means of production*, democratization of the workplace*, income distribution*, food and education for the poor* and peace and prosperity*??  Who knew?\n\nWow, I should subscribe.\n\n\n*Look those things up"

2 epochs \
P100 \
**highest toxicity** - "You are an idiot if you think privatizing Medicare will in any way benefit those of us who have paid into SS and Medicare our entire working lives."\
**lowest toxicity** - "Did you also complain about CMHC influencing house prices by insuring mortgages and thereby allowing borrowers to get lower mortgage rates?  I'm a big fan of zero government intervention in the housing market but that also means a typical borrower will pay 10% interest instead of 3%.  Sounds good to you?"

V100 \
**highest toxicity** - "you are a fool" \
**lowest toxicity** - "Good idea too have begun your comment with a c..."




