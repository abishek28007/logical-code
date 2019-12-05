def isValid(s):
  # if the string is empty it is valid
  if len(s) == 0:
    return True
  # if the string starts with a closing tag it's not valid
  elif s[0] in [')','}',']']:
    return False
  # map the opening tag with closing tag
  else :
    k = []
    for i in range(0,len(s)):
      if(s[i] == '(' or s[i] == '{' or s[i] == '['):
        k.append(s[i])
      elif(s[i] == ')' and k[len(k)-1] == '('):
        k.pop()
      elif(s[i] == '}' and k[len(k)-1] == '{'):
        k.pop()
      elif(s[i] == ']'and k[len(k)-1] == '['):
        k.pop()
  return len(k) == 0


print(isValid("()(){(())"))#False
print(isValid(""))#True
print(isValid("([{}])()"))#True
print(isValid(")[{}])()"))#False
print(isValid("({[)]"))#False