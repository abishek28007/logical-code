string = 'addafggffccddvvcc'#'asasaaaadfghj'
def fun(string):
	count = 0
	index = 0
	for i in range(0,len(string)-1):
		print 'i'+str(i)	
		if string[i]==string[i+1]:
			count +=1
			index = i
		elif string[i]!=string[i+1] and count>0:
			break
	print count, index
	if (count%2)!=0:
		print 'str1:'+string[:index-count+1]
		print 'str2:'+string[index+2:]
		fun(string[:index-count+1] + string[index+2:])
	else:	
		print string
print string
fun(string)
