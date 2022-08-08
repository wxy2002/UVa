lines=[]
while True:
    try:
        lines.append(input())
    except:
        break

def pal(s):
    for i in range(len(s)):
        if s[i]!=s[len(s) - 1 - i]:
            return 0
    return 1

mir_dic = {'A':'A', 'E':'3', 'H':'H', 'I':'I', 'J':'L', 'L':'J', 'M':'M', 'O':'O', 'S':'2', 'T':'T', 'U':'U', 'V':'V', 'W':'W', 'X':'X', 'Y':'Y', 'Z':'5', '1':'1', '2':'S',
'3':'E', '5':'Z', '8':'8'
}

def mir(s):
    for i in range(len(s)):
        if (s[i] not in mir_dic.keys()) or ((s[i] in mir_dic.keys()) and (mir_dic[s[i]]!=s[len(s) - 1 - i])):
            return 0
    return 1

for i in range(len(lines)):
    s = lines[i]
    flag_pal = pal(s)
    flag_mir = mir(s)
    if flag_pal==0 and flag_mir==0:
        print (s, '-- is not a palindrome.\n')
    if flag_pal==1 and flag_mir==0:
        print (s, '-- is a regular palindrome.\n')
    if flag_pal==0 and flag_mir==1:
        print (s, '-- is a mirrored string.\n')
    if flag_pal==1 and flag_mir==1:
        print (s, '-- is a mirrored palindrome.\n')