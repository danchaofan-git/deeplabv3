
f = open('results20220904-114603.txt', 'r')
f2 =open('results20220908-101421.txt', 'r')
f4 = open('loss.txt', 'r')
txt = f.readlines()
txt2 = f2.readlines()
txt3 = f4.readlines()
for i in range(0, 100):
    data = str(txt2[i])
    loss = str(txt3[i])
    txt[6 + i * 8] = 'mean IoU: ' + data
    txt[1 + i*8] = 'train_loss: ' + loss
with open('new_results.txt', 'w') as f3:
    for lines in txt:
        f3.write(str(lines))
print('111')