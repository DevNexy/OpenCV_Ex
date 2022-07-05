import numpy as np #넘파이 모듈 임포트

a = np.zeros((2, 5), np.int) #원소값 0 행렬 - 2행, 5열, 32비트 정수형
b = np.ones((3, 1), np.uint8) #원소값 1 행렬 - 3행, 1열, 부호없은 8비트 정수형
c = np.empty((1,5), np.float) #값없음 행렬 1행, 5열
d = np.full(5, 15, np.float32) #원소값 15, 1차원 행렬, 32비트 실수형

print(type(a), type(a[0]), type(a[0][0])) #객체 자료형, 객체 원소의 자료형 출력
print(type(b), type(b[0]), type(b[0][0]))
print(type(c), type(c[0]), type(c[0][0]))
print(type(d), type(d[0]))
print('c 형태:', c.shape, ' d 형태:', d.shape) #객체 형태 출력
print(a), print(b) #객체 원소 출력
print(c), print(d)