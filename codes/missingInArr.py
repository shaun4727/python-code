arr = [1,2,3]
n = 4
result = 0
for i in range(len(arr)):
    if i+1 == arr[i]:
        pass
    else:
        result = i+1
if result == 0:
    print(n)
else:
    print(result)