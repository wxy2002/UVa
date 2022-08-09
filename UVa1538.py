'''n = eval(input())
for i in range(n):
    num = eval(input())
    flag = 0
    if num-60<=0:
        start = 0
    else:
        start = num-60
    for j in range(start, num):
        s = str(j)
        sum = j
        for k in range(len(s)):
            sum = sum + eval(s[k])
        if sum==num:
            print (j)
            flag = 1
            break
    if flag==0:
        print (0)'''

# 你甚至可以采用打表的方法来解决问题
# 或者说只能用打表的方法...上面的那个TLE了

flag = []
for i in range(100001):
    flag.append(0)
for i in range(100001):
    s = str(i)
    sum = i
    for j in range(len(s)):
        sum = sum + eval(s[j])
    if sum<=100000 and flag[sum]==0:
        flag[sum] = i
n = eval(input())
for i in range(n):
    num = eval(input())
    print (flag[num])