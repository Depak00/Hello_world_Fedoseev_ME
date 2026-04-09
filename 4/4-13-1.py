a,b,c,d = [int(x) for x in input().split()]
if a<b:
    if a<c:
        if a<d:
            min=a
        else:
            min=d
    else:
        if c<d:
            min=c
        else:
            min=d
else:
    if b<c:
        if b<d:
            min=b
        else:
            min=d
    else:
        if c<d:
            min=c
        else:
            min=d
print(min)
