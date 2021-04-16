n,m=[int(i) for i in input().split()]
arr=[int(j) for j in input().split()]
A=[int(a) for a in input().split()]
A=set(A)
B=[int(b) for b in input().split()]
B=set(B)
h=0
for k in arr:
    if k in A:
        h+=1
    elif k in B:
        h-=1
print(h)
