B=0
A=1
m=int(input("input a number please "))
for k in range (1,m+1) :
    for i in range (1,k+1) :
    A=i*A
    B=B+A
print("this is your number",B)
