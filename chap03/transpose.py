import numpy as np
def function_array(row, col):
    output = np.array(np.arange(1, row * col + 1))
    output.shape = (output.size//col, col)
    for row in output:
        print("\t".join([str(x) for x in row]))
    return output

def transpose(array):
    output = np.transpose(array)
    for row in output:
        print("\t".join([str(x) for x in row]))

row = 3
col = 4
array = function_array(row, col)
array2 = transpose(array)