
def hn(n,a,b,c):
    if n>=1:
        hn(n-1,a,c,b)
        print(a,'->',c)
        hn(n-1,b,a,c)

#hn(3,'a','b','c')


def trim(s):
    i = len(s)
    while i > 0:
        if s[i - 1] == " ":
            i = i - 1
            if i == 0:
                s=''
        else:
            s = s[:i]
            break
    j = 0
    while j < i:
        if s[j] == " ":
            j = j + 1
        else:
            s = s[j:]
            break
    return s

print(trim(" abcdefg "))