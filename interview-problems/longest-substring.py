class Solution:
  def lengthOfLongestSubstring(self, s):
    outputStr = ''
    tempStr = ''
    for i in range(0, len(s)):
      if tempStr.find(s[i]) == -1:
        tempStr += s[i]
      elif tempStr.find(s[i]) != -1 and len(outputStr)<len(tempStr):
        outputStr = tempStr
        tempStr = s[i]
      else:
        tempStr = s[i]
    return len(outputStr)

print(Solution().lengthOfLongestSubstring('abrkaabcdefghijjxxx'))# 10
print(Solution().lengthOfLongestSubstring('jjxxx'))#2
