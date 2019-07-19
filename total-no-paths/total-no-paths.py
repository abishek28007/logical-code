def fun(rows, columns):
  k = [[0 for i in range(columns)] for j in range(rows)]
  if rows > 0:
    for i in range(0, rows):
      k[i][0] = 1
  if columns > 0:
    for j in range(0, columns):
      k[0][j] = 1
  if columns > 0 and rows > 0:
    for i in range(1, rows):
      for j in range(1, columns):
        k[i][j] = k[i-1][j] + k[i][j-1]
  # Debugging Purpose
  # for s in k:
  #   print(*s)
  print(k[rows-1][columns-1])


fun(4, 4)
fun(4, 1)
