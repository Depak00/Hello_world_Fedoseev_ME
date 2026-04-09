k = [int(x) for x in input().split()]
max=i=0
while i!=len(k):
    if k[i]>max:
        max=k[i]
    i+=1
print(max)
