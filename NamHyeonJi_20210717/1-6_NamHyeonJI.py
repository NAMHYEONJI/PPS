numRows = int(input())
array = [[] for row in range(numRows)]
for i in range(numRows):
    array[i] = [0] *(i+1)
    for j in range(i+1):
        if j == 0 or j == i:
            array[i][j] = 1
        else:
            array[i][j] = array[i-1][j-1] + array[i-1][j]




print(array)