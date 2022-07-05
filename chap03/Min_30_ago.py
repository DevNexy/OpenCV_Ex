#시간을 입력했을 때 30분 전의 시간을 출력하는 함수를 구현하시오.
def function_time(h, m):
    if m >= 30 :
        hour = h
        min = m-30
    else:
        minP = m-30
        min = minP + 60

        if h==1:
            hour = 12
        else:
            hour = h-1

    print("{}시 {}분 -> {}시 {}분".format(h,m,hour,min))

function_time(1, 10)