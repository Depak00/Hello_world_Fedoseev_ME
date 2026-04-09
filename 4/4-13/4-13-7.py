k = [int(x) for x in input().split()]
i=s=0
while i!=len(k):
  s+=i
  i+=1
s+=i
print(s/len(k))
