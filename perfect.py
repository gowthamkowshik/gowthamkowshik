n= int(input('how many keys:'))
l={}
i=1
k=int(input())
while(i*i<=k):
    if((k%i==0) and (n/i==0)):
       j='yes'
       l[k]=j
    else:
       j='no'
       l[k]=j
    i=i+1
print(l)
