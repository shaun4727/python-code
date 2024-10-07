arr = [7,2,1]
s = 2
A = []
n=3
curr_sum = arr[0]
start = 0

        # Add elements one by
        # one to curr_sum and
        # if the curr_sum exceeds
        # the sum, then remove
        # starting element
i = 1
while i <= n:

    # If curr_sum exceeds
    # the sum, then remove
    # the starting elements
    while curr_sum > s and start < i - 1:
        print(curr_sum,start,i)
        curr_sum = curr_sum - arr[start]
        start += 1

    # If curr_sum becomes
    # equal to sum, then
    # return true
    if curr_sum == s:
        A.append(start + 1)
        A.append(i)
        break

    # Add this element
    # to curr_sum
    if i < n:
        curr_sum = curr_sum + arr[i]
    i += 1


print(A)