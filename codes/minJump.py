# arr = [1, 2, 1, 1, 6, 7]
# arr = [9, 10, 1, 2 ,3 ,4 ,8 ,0, 0, 0 ,0, 0, 0, 0, 1]
# arr = [2,1,0,3,5,1,2]
# arr = [1,3,5,8,9,2,6,7,6,8,9]
# arr = [1,4,3,2,6,7]
# arr = [10, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
arr = [3, 2, 1, 1, 0, 5]


jump = 1
stair = arr[0]
i = 1
Max = arr[0]

while i < len(arr):
    if i+1 == len(arr):
        break
    if i + arr[i] > Max:
        Max = i + arr[i]
  
    stair -= 1
    if stair == 0:
        jump += 1
        stair = Max - i


    i += 1

if stair>0:
    print(jump)
else:
    print(-1)

