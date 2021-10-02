import numpy as np 
import math


rows = int(input("Enter Number of rows"))
value = int(input("Enter the Value til you want to count"))
activated_row = 0
number = 1
result = np.zeros((rows,value), dtype=int)
str1 = ""

for x in range(value):
    for y in range(rows):
        if(activated_row == y):
            result[y][x] = number
            number = number + 1
    if((math.floor(x/(rows-1))) % 2 == 0 ):
        activated_row = activated_row + 1
    else:
        activated_row = activated_row - 1
    


for ele in result:
    for num in ele:
        if(num == 0):
            str1 = str1 + " "
        else:
            str1 = str1 + str(num)
    print(str1)
    str1 = ""


