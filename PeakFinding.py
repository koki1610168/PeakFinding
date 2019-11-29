"""
2-dimentional(n*m) peak finding
compleity: O()
time measure: T()
wost complexity = O(n*m)

Attempt
Pick middle column: j = m/2
Find global max on column: i
(i, j)
Compare (i, j-1), (i, j), (i, j+1)

if (i, j-1) < (i, j) > (i, j+1)
    (i, j) is 2D peak
else if (i, j-1) > (i, j)
    search left
else if (i, j+1) > (i, j)
    search right

[[3, 4, 5, 6],
 [7, 8, 9, 10],
 [11, 12, 13, 14]]
"""
import random
import time
import math


rows = int(input("How many rows: "))
columns = int(input("How many columns: "))
Max = int(input("put a max number: "))
arr = []
oneD_arr = []
for j in range(columns):
    for i in range(rows):
        oneD_arr.append(random.randint(1, Max))
        if len(oneD_arr) == rows:
            arr.append(oneD_arr)
            oneD_arr = []


def findMax(arr, row, column, mid, max_num=0):
    for i in range(row):
        if (max_num < arr[i][mid]):
            max_num = arr[i][mid]
            max_index = i
    return max_num, max_index
            
def findPeak(arr, row, column, mid):
    max_num, max_index= findMax(arr, row, column, mid)
    
    if mid == 0 or mid == column-1:
        return max_num
    
    
    if arr[max_index][mid-1] <= max_num and max_num >= arr[max_index][mid+1]:
        return max_num
    
    if arr[max_index][mid-1] > arr[max_index][mid]:
        return findPeak(arr, row, column, mid-math.ceil(mid/2.0))

    if arr[max_index][mid+1] > arr[max_index][mid]:
        return findPeak(arr, row, column, mid+math.ceil(mid/2.0))
    
    

print(arr)
start = time.time()
highest = findPeak(arr, rows, columns, columns//2)
end = time.time()
print(highest)
print(end-start)

    
