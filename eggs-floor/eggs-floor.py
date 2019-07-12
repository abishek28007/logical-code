def fun(egg,floor):
  if floor == 1:
    print(floor)
  elif egg == 1:
    print(floor)
  else:
    for i in range(1,floor):
      if i*i + i >= 2*floor:
        break
    print(i)

fun(3,100)
fun(1,100)
fun(3,1)