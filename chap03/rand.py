#[1,50] 범위안의 정수형 숫자 1000개를 생성하고 그중 가장 빈도수가 높은 수를 출력하시오.
from random import randint

#난수 1000개 생성
numbers = [randint(1, 50) for i in range(1000)]

cnt = [] #빈 리스트 생성

for i in range(51):
    cnt.append(0)

print(cnt)

for i in numbers:
    cnt[i] += 1

print(cnt)
print(cnt.index(max(cnt)))