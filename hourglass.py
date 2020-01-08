#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the hourglassSum function below.
def hourglassSum(arr,i,j):
    return (arr[i][j] + arr[i][j+1] + arr[i][j+2] + arr[i+1][j+1] + arr[i+2][j] +arr[i+2][j+1] + arr[i+2][j+2])


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr = []

    for _ in range(6):
        arr.append(list(map(int, input().rstrip().split())))

    list_new = []

    for j in range(len(arr)-2):
        for i in range(len(arr)-2):
            result = hourglassSum(arr,i,j)
            list_new.append(result)
    max_num = max(list_new)
    
    #print(max(list_new))
        #return max_num

   # result = hourglassSum(arr)

    fptr.write(str(max_num) + '\n')

    fptr.close()
