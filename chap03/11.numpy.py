import numpy as np

list1, list2 = [1,2,3], [4, 5.0, 6] #리스트 생성
a, b = np.array(list1), np.array(list2) #리스트로 ndarray 객체 생성

c = a + b #ndarray 객체 연산 - np.add(list1, list2)
d = a - b #np.subtract(list1, list2)
e = a * b #np.multiply(list1, list2)
f = a / b #np.divide(list1, list2)
g = a * 2 #스칼라 곱
h = b + 2 #스칼라 합

print('a 자료형:', type(a), type(a[0])) #결과 출력
print('b 자료형:', type(b), type(b[0]))
print('c 자료형:', type(c), type(c[0]))
print('g 자료형:', type(g), type(g[0]))
print(c, d, e)
print(f, g, h)