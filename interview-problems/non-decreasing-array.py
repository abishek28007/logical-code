def check(lst):
  flag = 0
  for i in range(1,len(lst)-1):
    if(lst[i-1]>lst[i] and lst[i]>lst[i+1]):
      flag += 1
      break
    # elif lst[i] > lst[i+1]:
    #   if(lst[])
    #   flag +=1
  # Fill this in.
  return flag

#Can you find a solution in O(n) time?
print(check([13, 4, 7]))
# True
print(check([5,1,3,2,5]))
# False