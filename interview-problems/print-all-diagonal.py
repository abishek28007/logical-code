def funcDiagonal(arr):
    for i in range(0,2*len(arr)-1): # 2*(4-1) = 6
        if(i<len(arr)):
            a = 0
            while a<= i:
                b = i-a
                # print(str(b), end='')
                # print(str(a), end='')
                print(arr[b][a], end='')
                print(' ', end='')
                a +=1
        else:
            a = i - (len(arr)-1)
            while a<= len(arr)-1:
                b = i-a
                # print(str(b), end='')
                # print(str(a), end='')
                print(arr[b][a], end='')
                print(' ', end='')
                a +=1
        print()

arr3 = [
    [1,2,3,4],
    [5,6,7,8],
    [9,10,11,12],
    [13,14,15,16]
]

arr = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]

funcDiagonal(arr3)

# 1           0,0                 0
# 5 2         1,0 0,1             1
# 9 6 3       2,0 1,1 0,2         2
# 13 10 7 4   3,0 2,1 1,2 0,3     3
# 14 11 8     3,1 2,2 1,3         4
# 15 12       3,2 2,3             5
# 16          3,3                 6

# 1           0,0
# 4 2         1,0 0,1
# 7 5 3       2,0 1,1 0,2
# 8 6         2,1 1,2
# 9           2,2