Number = int(input("Please Enter the Fibonacci Numbers Range = "))
First = 0
Second = 1
Sum = 0
i = 0
while(i <  Number):
    print(First, end = '  ')
    Sum = Sum + First
    Next = First + Second
    First = Second
    Second = Next
    i = i + 1
print("\nThe Sum of Fibonacci Series Numbers = %d" %Sum)
