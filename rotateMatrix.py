# You are given a n x n 2D matrix A representing an image.
# Rotate the image by 90 degrees (clockwise).
# PS: You aren't allowed to create an additional array
# Input
# [ [1, 2],[3, 4]]
# Output
# [[3, 1],[4, 2]]

def rotateMatrix(row,column,matrix):
    for i in range(row):
        for j in range(i+1,column):
            matrix[i][j],matrix[j][i]=matrix[j][i],matrix[i][j]
    for i in matrix:
        reversedmatrix=[]
        # for j in range(1,column):
        #    matrix[i][column-i],matrix[column-i][i]=matrix[column-i][i],matrix[i][column-i]
        reversedmatrix.append(i[::-1])
    return reversedmatrix


matrix=[]
row=int(input())
column=int(input())
for i in range(row):
    matrix.append(list(map(int,input().split())))
print(rotateMatrix(row,column,matrix))