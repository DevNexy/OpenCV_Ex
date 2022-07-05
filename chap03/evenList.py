#100 이하의 짝수가 들어있는 리스트를 생성하고 for문을 이용하여 역순으로 출력하시오.
even = []

for i in range(2,101,2):
    even.append(i)
print(even)
print(even[::-1])