n = eval(input())
for i in range(n):
    s = input()
    flag = 0
    score = 0
    for j in range(len(s)):
        if s[j]=='O':
            flag += 1
        else:
            flag = 0
        score += flag
    print (score)