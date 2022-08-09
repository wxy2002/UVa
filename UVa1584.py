n = eval(input())

for i in range(n):
    s = input()
    # print (s)
    ans = s
    s = s * 2
    for j in range(1, len(s)//2):
        now_s = s[j:(len(s)//2 + j)]
        if now_s < ans:
            ans = now_s
    print (ans)