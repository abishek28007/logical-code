# def binarySearch(arr, l, r, x):
#     if r >= l:
#         mid = l + int((r - l)/2)
#         # If element is present at the middle itself
#         if arr[mid] == x:
#             return mid
#         # If element is smaller than mid, then it
#         # can only be present in left subarray
#         elif arr[mid] > x or arr[mid-1] == x:
#           return binarySearch(arr, l, mid-1, x)
#         # Else the element can only be present
#         # in right subarray
#         elif arr[mid] < x or arr[mid+1] == x:
#           return binarySearch(arr, mid + 1, r, x)
#     else:
#         # Element is not present in the array
#         return -1

def firstandlast(arr, n):
  first = -1
  last = -1
  #First occurance
  beg = 0
  end = len(arr) - 1
  while (beg <= end):
    mid = beg + int((end-beg)/2)
    if (arr[mid] == n):
      if (mid-1 >= 0 and arr[mid-1] == n):
        end = mid-1
        continue
      first = mid
      break
    elif (arr[mid] < n):
      beg = mid + 1
    else:
      end = mid - 1
  #Last occurance
  beg = 0
  end = len(arr) - 1
  while (beg <= end):
    mid = beg + int((end-beg)/2)
    if (arr[mid] == n) :
        if (mid+1 <= len(arr) and  arr[mid+1] == n) :
          beg = mid + 1
          continue
        last = mid
        break
    elif (arr[mid] < n):
        beg = mid + 1  
    else:
        end = mid - 1
  return [first,last]

# Function call 
print(firstandlast([1,3,3,5,7,8,9,9,9,15],9))
print(firstandlast([100, 150, 150, 153],150))
print(firstandlast([1,2,3,4,5,6,10],9))
