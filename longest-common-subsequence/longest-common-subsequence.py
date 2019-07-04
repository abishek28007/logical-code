def fun(firstStr, secondStr):
  n = len(firstStr)
  m = len(secondStr)
  k = [[0 for i in range(m+1)] for j in range(n+1)]
  for i in range(0,n):
    for j in range(0,m):
      if firstStr[i]==secondStr[j]:
        k[i+1][j+1] = k[i][j]+1
      else:
        k[i+1][j+1] = k[i][j+1] if k[i][j+1] > k[i+1][j] else k[i+1][j]
  for s in k:
    print(*s)

fun('ACBDEA','ABCDA')