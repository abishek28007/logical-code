# N = 999 -> 9+9+9 = 27-> 2+7 = 9
# N = 789 -> 7+8+9= 24-> 2+4 = 6
def funcSum(num):
    s=0
    if(num < 10):
        return num
    while num > 0:
        s += num%10
        num //= 10
    return funcSum(s)
print(funcSum(999))
print(funcSum(789))