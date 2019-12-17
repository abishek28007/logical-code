def singleNumber(nums):
  num = 0
  for i in range(len(nums)):
    num ^= nums[i]
  return num

print(singleNumber([4, 3, 2, 4, 1, 3, 2, 8, 8, 8, 8]))