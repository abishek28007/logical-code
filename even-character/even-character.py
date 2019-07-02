def fun(string):
	k=0
	while(k<len(string)):
		count = 1
		for i in range(k,len(string)-1):
			if string[i] == string[i+1]:
				count += 1
			else:
				break
		if count%2 == 0 and i+count != len(string):
			string = string[:i-count+1] + string[i+1:]
			k =-1
		elif count%2 == 0:
			string = string[:i-count+2] + string[i+2:]
			k =-1
		else:
			k += count-1
		k+=1
	print(string)

fun('abbbaacd')
fun('addafggffccddvvcc')
fun('asasaaaadfghj')
fun('aa')