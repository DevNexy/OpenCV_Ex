# 구구단을 2단부터 9단까지 모두 출력하시요.(반복문 사용)
for i in range(2, 10):
    print()
    print(i,'단')
    for j in range(1, 10):
        dan = i * j
        print(i, 'x', j,'=',dan)