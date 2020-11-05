def funcLatest(A, B):
    version_a = list(map(int,A.split('.')))
    version_b = list(map(int,B.split('.')))
    i = 0
    j = 0
    output = 'A and B are same'
    while (i < len(version_a) and j < len(version_b)):
        if version_a[i] > version_b[j]:
            output = 'A is Latest'
            break
        elif version_a[i] < version_b[j]:
            output = 'B is Latest'
            break
        i+=1
        j+=1
    while(i < len(version_a)):
        if(version_a[i]>0):
            output = 'A is Latest'
            break
        else:
            i+=1
    while(j < len(version_b)):
        if(version_b[j]>0):
            output = 'B is Latest'
            break
        else:
            j+=1
    return output

print(funcLatest('2.2.0.0.1', '2.2.1'))# Given version B latest than version A
print(funcLatest('2.2.0.0.1', '2.2.0'))# Given version A latest than version B
print(funcLatest('2.2.0', '2.2'))# Given versions are the same
print(funcLatest('1.2.1', '1.2.1'))# Given versions are the same
print(funcLatest('1.1.0', '1.1.1'))# Given version B latest than version A