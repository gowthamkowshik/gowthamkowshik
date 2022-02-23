l = eval(input("Enter the list: "))
start = int(input("Enter start index: "))
stop = int(input("Enter stop index: "))

slice = l[start : stop + 1]
mx = max(slice)
mi = min(slice)

print("Maximum =", mx)
print("Minimum =", mi)
