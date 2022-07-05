import numpy as np

list = [1.0, 2.0, 3.0, 4.0, 5.0, 6.0, 7.0, 8.0, 9.0, 10.0]
arr = np.array(list)
sum = 0

for i in range(0, 10):
        sum += arr[i]

print('합: {:.2f}'.format(sum))

avg = sum/10

print('평균: {:.2f}'.format(avg))