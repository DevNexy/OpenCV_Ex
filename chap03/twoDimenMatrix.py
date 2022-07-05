#이중 포문을 사용하여 아래와 같은 2차원 행렬을 출력하는 함수를 구현하시오(ndarray 자료형 이용)
import numpy as np

def function_array(row, col):
    output = np.array(np.arange(1, row * col + 1))
    output.shape = (output.size//col, col)
    for row in output:
        print("\t".join([str(x) for x in row]))
    return output

row = 3
col = 4
array = function_array(row, col)