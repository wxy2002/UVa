wrongstr = "`1234567890-=QWERTYUIOP[]\ASDFGHJKL;'ZXCVBNM,./"

lines=[]
while True:
    try:
        lines.append(input())
    except:
        break 

def do_line(in_str):
    for i in range(len(in_str)):
        x = wrongstr.find(in_str[i])
        if x == -1:
            print (in_str[i], end='')
        else:
            print (wrongstr[x-1], end='')
    print ('')

for i in range(len(lines)):
    do_line(lines[i])