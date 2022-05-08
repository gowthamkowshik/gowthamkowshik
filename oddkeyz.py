n=int(input("Enter keys:"))
l={}
for i in range(1,n):
    g=int(input())
    if i%2==0:
        j='yes'
        l[g]=j
    else:
        j='no'
        l[g]=j
print(l)
