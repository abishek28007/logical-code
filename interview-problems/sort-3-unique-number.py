def sortNums(nums):
  one_idx = 0 # Represents the leftmost index that is not 0
  three_idx = len(nums) - 1 # Represents the rightmost index that is not 2
  idx = 0 # Represents the index that we are checking
  while idx <= three_idx:
    print(*nums, idx, one_idx, three_idx)
    if nums[idx] == 1:
      # Swap numbers with leftmost index
      # so all numbers up to one_idx are all 1
      nums[idx], nums[one_idx] = nums[one_idx], nums[idx]
      idx += 1
      one_idx += 1
    elif nums[idx] == 2:
      # If index is 2, it means list is in order, check next number
      idx += 1
    elif nums[idx] == 3:
      # Swap numbers with rightmost index
      # so all numbers after three_idx are all 3
      nums[idx], nums[three_idx] = nums[three_idx], nums[idx]
      three_idx -= 1
  return nums

print(sortNums([3, 3, 2, 1, 3, 2, 1]))
print(sortNums([3, 3, 2, 1, 3, 3, 3]))

