year = 2020

if(year % 4 == 0) and (year % 100 != 0): #4년마다 윤년, 10년마다 윤년 아님
    print(year, "는 윤년입니다.")
elif year % 400 ==0: #400년마다 윤년
    print(year, "는 윤년입니다.")
else:
    print(year, "는 윤년이 아닙니다.")