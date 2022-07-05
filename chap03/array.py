#실수형 원소 10개를 갖는 ndarray 행렬을 선언해서 전체 원소의 합과 평균을 직접 구하는 함수를 구현하시오.
#합과 평균은 소수점 둘째 자리까지 나타내시오.
import numpy as np

list = [1.0, 2.0, 3.0, 4.0, 5.0, 6.0, 7.0, 8.0, 9.0, 10.0]
a = np.array(list)
sum = 0

for i in range(0, 10):
    sum += a[i]

print('합: {:.2f}'.format(sum))

avg = sum / 10

print('평균: {:.2f}'.format(avg))