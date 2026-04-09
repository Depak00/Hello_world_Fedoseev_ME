k = [int(x) for x in input().split()]
s=i=0
while i!=len(k):
  if k[i]%2==1:
    s+=k[i]
s+=k[i]
print(s)
