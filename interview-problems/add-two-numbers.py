# Definition for singly-linked list.
class ListNode(object):
  def __init__(self, x):
    self.val = x
    self.next = None

class Solution:
  def getnum(self,listRef):
    num = 0 
    i = 0
    while listRef: 
      num = num + listRef.val*(10**i)
      listRef = listRef.next
      i += 1
    return num

  def addTwoNumbers(self, l1, l2):
    first = self.getnum(l1)
    second = self.getnum(l2)
    sum = first+second
    result = head = ListNode(sum % 10) # since head needs to be assigned a value once
    sum = sum/10
    while sum > 0:
      s = int(sum%10)
      sum = int(sum/10)
      result.next = ListNode(s)
      result = result.next
    return head

l1 = ListNode(2)
l1.next = ListNode(4)
l1.next.next = ListNode(3)

l2 = ListNode(5)
l2.next = ListNode(6)
l2.next.next = ListNode(4)

result = Solution().addTwoNumbers(l1, l2)
while result:
  print(result.val),
  result = result.next
# 7 0 8
