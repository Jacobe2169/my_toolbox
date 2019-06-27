import copy
import numpy as np

def matrix_pretty_print(mat):
    col_maxes = [max([len(("{0}").format(x)) for x in col]) for col in mat.T]
    for x in mat:
        for i, y in enumerate(x):
            print(("{:"+str(col_maxes[i])+"}").format(y), end="  ")
        print("")

def matrix_pretty_print_with_axis_labels(matrix,labels):
    res = np.concatenate((np.array([[l] for l in labels]),matrix),axis=1)
    ext_label=copy.copy(labels);ext_label.insert(0,"X")
    res= np.concatenate((np.array([ext_label]),res),axis=0)
    matrix_pretty_print(res)
    
