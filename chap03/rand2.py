#0~50 사이의 임의의 원소(정수형,중복가능)을 500개 만들어서
#가장 중복이 많이 나온 원소 3개를 원소 값과 중복 횟수로 출력하시오.
import numpy as np
from random import randint

rand = [] #500개 랜덤
rand2 = [] #빈 리스트

rand =[randint(0,50) for i in range(500)]

for i in range(51):
    rand2.append(0)
print(rand)
print(rand2)

for i in rand:
    rand2[i-1] += 1

print(rand2)

for i in range(3):
    max_value = rand2.index(max(rand2))  # 최댓값
    print("원소 값",max_value,"중복 횟수",rand2[max_value])
    del rand2[max_value]
