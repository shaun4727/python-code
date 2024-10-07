



arr = [-1, 2, 3, -2, 5]
size = len(arr)
max_so_far = -9999999 - 1
max_ending_here = 0
stack = []

#Iterating over the array.
for i in range(0, size):
    #Updating max sum till current index.
    max_ending_here = max_ending_here + arr[i]
    stack.append(arr[i])

    #Storing max sum so far by choosing maximum between max
    #sum so far and max sum till current index.
    if (max_so_far < max_ending_here):
        max_so_far = max_ending_here

    #If max sum till current index is negative, we do not need to add
    #it to result so we update it to zero.
    if max_ending_here < 0:
        max_ending_here = 0
        stack = []

print(max_so_far)
print(stack)