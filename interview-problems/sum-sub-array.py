def sum(lst):
  s = 0
  sumList = [len(lst)]
  prodList = [len(lst)] * len(lst)
  isEven = True if len(lst)%2 == 0 else False
  n = int(len(lst)/2)
  if(not isEven):
    n += 1
  # for i in range(1,n):
  #   sumList.append(sumList[i-1]- 2)
  #   prodList[i]= prodList[i-1]+sumList[i]
  #   prodList[len(lst)-i-1] = prodList[i]
  # for j in range(0,len(prodList)):
  #   s+= lst[j]*prodList[j]
  for i in range(0,n):
    sumList.append(sumList[i]- 2)
    prodList[i+1]= prodList[i]+sumList[i+1]
    prodList[len(lst)-1-i] = prodList[i]
    s += lst[i]*prodList[i]
    if(i != len(lst)-1-i):
      s += prodList[len(lst)-1-i]*lst[len(lst)-1-i]

# Every element lst[i] appears in two types of subsets:
# i)  In subarrays beginning with lst[i]. There are 
#     (n-i) such subsets. For example [2] appears
#     in [2] and [2, 3].
# ii) In (n-i)*i subarrays where this element is not
#     first element. For example [2] appears in 
#     [1, 2] and [1, 2, 3].

# Total of above (i) and (ii) = (n-i) + (n-i)*i 
#                             = (n-i)(i+1)
  # for i in range(0, n): 
	# 	s += (lst[i] * (i+1) * (n-i)) 
  return s

#Can you find a solution in O(n) time?
print(sum([1, 2]))
# 6
# {1} + {2} + {1 + 2}

# 1 -> 2
# 2 -> 2

# 2 2

print(sum([1, 2, 3]))
# 20
# {1} + {2} + {3} + {2 + 3} + {1 + 2} + {1 + 2 + 3}

# 1 -> 3
# 2 -> 4 -> 1
# 3 -> 3

# 3 1 3
# 3 4 3

print(sum([1,2,3,4]))
# 50
# {1+2+3+4} + {1+2+3} + {2+3+4} + {1+2} + {2+3} + {3+4} + {1} + {2} + {3} + {4}

# 1 -> 4
# 2 -> 6 -> 2
# 3 -> 6 -> 2
# 4 -> 4

# 4 2 2 4
# 4 6 6 4

print(sum([1,2,3,4,5]))
# 105
# {1+2+3+4+5} + {1+2+3+4} + {2+3+4+5} + {1+2+3} + {2+3+4} + {3+4+5} + {1+2} + {2+3} + {3+4} + {4+5} + {1} + {2} + {3} + {4} + {5}

# 1 -> 5
# 2 -> 8 -> 3
# 3 -> 9 -> 4 -> 1
# 4 -> 8 -> 3
# 5 -> 5

# 5 3 1 3 5
# 5 8 9 8 5

print(sum([1,2,3,4,5,6]))
# 196
# {1} + {1 + 2} + {1 + 2 + 3} + {1 + 2 + 3 + 4} + {1 + 2 + 3 + 4 + 5} + {1 + 2 + 3 + 4 + 5 + 6} + {2} + {2 + 3} + {2 + 3 + 4} + {2 + 3 + 4 + 5} + {2 + 3 + 4 + 5 + 6} + {3} + {3 + 4} + {3 + 4 + 5} + {3 + 4 + 5 + 6} + {4} + {4 + 5} + {4 + 5 + 6} + {5} + {5 + 6} + {6} 

# 1 -> 6
# 2 -> 10 -> 4
# 3 -> 12 -> 6 -> 2
# 4 -> 12 -> 6 -> 2
# 5 -> 10 -> 4
# 6 -> 6

# 6  4  2  2  4 6
# 6 10 12 12 10 6