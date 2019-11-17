def fun(n,steps):
    validStep = list(filter(lambda x: x <= n, steps))
    if n==0:
        return 1
    else:
        count = 0
        for i in validStep:
            count += fun(n-i,steps)
    return count


print(fun(4,[1,2]))
print(fun(3,[1,2,3]))
