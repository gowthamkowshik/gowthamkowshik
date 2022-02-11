sno=int(input('enter number'))
sname=input('enter name')
sgroup=input('enter group')
s1=int(input('enter telugu marks'))
s2=int(input('enter hindi marks'))
s3=int(input('enter english marks'))
s4=int(input('enter maths marks'))
s5=int(input('enter science marks'))
s6=int(input('enter social marks'))
total=s1+s2+s3+s4+s5+s6
avg=total%6
if(avg>=91):
  print('O grade')
elif(avg>=81):
  print('A grade')
elif(avg>=71):
  print('B grade')
elif(avg>=60):
  print('C grade')
elif(avg>=50):
  print('D grade')
elif(avg>=40):
  print('pass')
else:
 print('fail')
