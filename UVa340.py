# 真的看不懂题干的表述和样例的关系

def str_input():
    s = input().split(' ')
    num = []
    for i in range(len(s)):
        num.append(eval(s[i]))
    return num

n = eval(input())
num = 0
while (n!=0):
    num = num + 1
    ans = str_input()
    print ("Game %d:"%(num))
    guess = str_input()
    while sum(guess)!=0:
        A = 0; B = 0; flag = []
        for i in range(len(guess)):
            if guess[i]==ans[i]:
                A += 1
                flag.append(guess[i])
        for i in range(len(guess)):
            if (guess[i] in ans) and (guess[i] not in flag):
                B += 1
        print ('    (%d,%d)'%(A, B))
        guess = str_input()
    n = eval(input())
