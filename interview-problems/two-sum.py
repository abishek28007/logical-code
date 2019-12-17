def two_sum(list, k):
  list.sort()
  rhs = len(list)-1
  lhs = 0
  # sort the array and them walk inward
  while lhs < rhs:
    if k == list[lhs]+list[rhs]:
      return True
    elif k > list[lhs]+list[rhs]:
      lhs += 1
    else:
      rhs -= 1
  return False

print(two_sum([4,7,1,-3,2], 5))
